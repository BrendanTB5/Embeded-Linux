/**
 * @file   gpio_test.c
 * @author Derek Molloy
 * @date   19 April 2015
 * @brief  A kernel module for controlling a GPIO LED/button pair. The device mounts devices via
 * sysfs /sys/class/gpio/gpio115 and gpio49. Therefore, this test LKM circuit assumes that an LED
 * is attached to GPIO 49 which is on P9_23 and the button is attached to GPIO 115 on P9_27. There
 * is no requirement for a custom overlay, as the pins are in their default mux mode states.
 * @see http://www.derekmolloy.ie/
*/

#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/gpio.h>                 // Required for the GPIO functions
#include <linux/interrupt.h>            // Required for the IRQ code

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Derek Molloy");
MODULE_DESCRIPTION("A Button/LED test driver for the BBB");
MODULE_VERSION("0.6");

static unsigned int gpioLED1 = 60;       ///< hard coding the LED gpio for this example to P9_16 (GPIO51)
static unsigned int gpioButton1 = 47;   ///< hard coding the button gpio for this example to P9_27 (GPIO115)
static unsigned int gpioLED2 = 50;
static unsigned int gpioButton2 = 65;
static unsigned int irq1Number;          ///< Used to share the IRQ number within this file
static unsigned int irq2Number;          ///< Used to share the IRQ number within this file
static unsigned int numberPresses1 = 0;  ///< For information, store the number of button presses
static unsigned int numberPresses2 = 0;  ///< For information, store the number of button presses
static bool led1On = 0;   ///< Is the LED on or off? Used to invert its state (off by default)
static bool led2On = 0;

/// Function prototype for the custom IRQ handler function -- see below for the implementation
static irq_handler_t  ebbgpio_irq_handler1(unsigned int irq, void *dev_id, struct pt_regs *regs);
static irq_handler_t  ebbgpio_irq_handler2(unsigned int irq, void *dev_id, struct pt_regs *regs);

/** @brief The LKM initialization function
 *  The static keyword restricts the visibility of the function to within this C file. The __init
 *  macro means that for a built-in driver (not a LKM) the function is only used at initialization
 *  time and that it can be discarded and its memory freed up after that point. In this example this
 *  function sets up the GPIOs and the IRQ
 *  @return returns 0 if successful
 */
static int __init ebbgpio_init(void){
   int result = 0;
   printk(KERN_INFO "GPIO_TEST: Initializing the GPIO_TEST LKM\n");
   // Is the GPIO a valid GPIO number (e.g., the BBB has 4x32 but not all available)
   if (!gpio_is_valid(gpioLED1)){
      printk(KERN_INFO "GPIO_TEST: invalid LED GPIO\n");
      return -ENODEV;
   }
   if (!gpio_is_valid(gpioLED2)){
      printk(KERN_INFO "GPIO_TEST: invalid LED GPIO\n");
      return -ENODEV;
   }
   // Going to set up the LED. It is a GPIO in output mode and will be on by default
   led1On = false;
   led2On = false;
   gpio_request(gpioLED1, "sysfs");          // gpioLED is hardcoded to 51, request it
   gpio_direction_output(gpioLED1, led1On);   // Set the gpio to be in output mode and on
// gpio_set_value(gpioLED, ledOn);          // Not required as set by line above (here for reference)
   gpio_export(gpioLED1, false);             // Causes gpio51 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed
   gpio_request(gpioButton1, "sysfs");       // Set up the gpioButton
   gpio_direction_input(gpioButton1);        // Set the button GPIO to be an input
   gpio_set_debounce(gpioButton1, 200);      // Debounce the button with a delay of 200ms
   gpio_export(gpioButton1, false);          // Causes gpio115 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed
   // Perform a quick test to see that the button is working as expected on LKM load
   printk(KERN_INFO "GPIO_TEST: The button1 state is currently: %d\n", gpio_get_value(gpioButton1));

   // GPIO numbers and IRQ numbers are not the same! This function performs the mapping for us
   irq1Number = gpio_to_irq(gpioButton1);
   printk(KERN_INFO "GPIO_TEST: The button1 is mapped to IRQ: %d\n", irq1Number);

   // This next call requests an interrupt line
   result = request_irq(irq1Number,             // The interrupt number requested
                        (irq_handler_t) ebbgpio_irq_handler1, // The pointer to the handler function below
                        IRQF_TRIGGER_RISING | IRQF_TRIGGER_FALLING,   // Interrupt on rising edge (button press, not release)
                        "ebb_gpio_handler",    // Used in /proc/interrupts to identify the owner
                        NULL);                 // The *dev_id for shared interrupt lines, NULL is okay

   printk(KERN_INFO "GPIO_TEST: The interrupt 1 request result is: %d\n", result);
   
   gpio_request(gpioLED2, "sysfs");          // gpioLED is hardcoded to 51, request it
   gpio_direction_output(gpioLED2, led2On);   // Set the gpio to be in output mode and on
// gpio_set_value(gpioLED, ledOn);          // Not required as set by line above (here for reference)
   gpio_export(gpioLED2, false);             // Causes gpio51 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed
   gpio_request(gpioButton2, "sysfs");       // Set up the gpioButton
   gpio_direction_input(gpioButton2);        // Set the button GPIO to be an input
   gpio_set_debounce(gpioButton2, 200);      // Debounce the button with a delay of 200ms
   gpio_export(gpioButton2, false);          // Causes gpio115 to appear in /sys/class/gpio
			                    // the bool argument prevents the direction from being changed
   // Perform a quick test to see that the button is working as expected on LKM load
   printk(KERN_INFO "GPIO_TEST: The button2 state is currently: %d\n", gpio_get_value(gpioButton2));

   // GPIO numbers and IRQ numbers are not the same! This function performs the mapping for us
   irq2Number = gpio_to_irq(gpioButton2);
   printk(KERN_INFO "GPIO_TEST: The button2 is mapped to IRQ: %d\n", irq2Number);

   // This next call requests an interrupt line
   result = request_irq(irq2Number,             // The interrupt number requested
                        (irq_handler_t) ebbgpio_irq_handler2, // The pointer to the handler function below
                        IRQF_TRIGGER_RISING | IRQF_TRIGGER_FALLING,   // Interrupt on rising edge (button press, not release)
                        "ebb_gpio_handler",    // Used in /proc/interrupts to identify the owner
                        NULL);                 // The *dev_id for shared interrupt lines, NULL is okay

   printk(KERN_INFO "GPIO_TEST: The interrupt 2 request result is: %d\n", result);
   
   
   return result;
}

/** @brief The LKM cleanup function
 *  Similar to the initialization function, it is static. The __exit macro notifies that if this
 *  code is used for a built-in driver (not a LKM) that this function is not required. Used to release the
 *  GPIOs and display cleanup messages.
 */
static void __exit ebbgpio_exit(void){
   printk(KERN_INFO "GPIO_TEST: The button1 state is currently: %d\n", gpio_get_value(gpioButton1));
   printk(KERN_INFO "GPIO_TEST: The button1 was pressed %d times\n", numberPresses1);
   gpio_set_value(gpioLED1, 0);              // Turn the LED off, makes it clear the device was unloaded
   gpio_unexport(gpioLED1);                  // Unexport the LED GPIO
   free_irq(irq1Number, NULL);               // Free the IRQ number, no *dev_id required in this case
   gpio_unexport(gpioButton1);               // Unexport the Button GPIO
   gpio_free(gpioLED1);                      // Free the LED GPIO
   gpio_free(gpioButton1);                   // Free the Button GPIO
   
   
   printk(KERN_INFO "GPIO_TEST: The button2 state is currently: %d\n", gpio_get_value(gpioButton2));
   printk(KERN_INFO "GPIO_TEST: The button2 was pressed %d times\n", numberPresses2);
   gpio_set_value(gpioLED2, 0);              // Turn the LED off, makes it clear the device was unloaded
   gpio_unexport(gpioLED2);                  // Unexport the LED GPIO
   free_irq(irq2Number, NULL);               // Free the IRQ number, no *dev_id required in this case
   gpio_unexport(gpioButton2);               // Unexport the Button GPIO
   gpio_free(gpioLED2);                      // Free the LED GPIO
   gpio_free(gpioButton2);                   // Free the Button GPIO
   printk(KERN_INFO "GPIO_TEST: Goodbye from the LKM!\n");
}

/** @brief The GPIO IRQ Handler function
 *  This function is a custom interrupt handler that is attached to the GPIO above. The same interrupt
 *  handler cannot be invoked concurrently as the interrupt line is masked out until the function is complete.
 *  This function is static as it should not be invoked directly from outside of this file.
 *  @param irq    the IRQ number that is associated with the GPIO -- useful for logging.
 *  @param dev_id the *dev_id that is provided -- can be used to identify which device caused the interrupt
 *  Not used in this example as NULL is passed.
 *  @param regs   h/w specific register values -- only really ever used for debugging.
 *  return returns IRQ_HANDLED if successful -- should return IRQ_NONE otherwise.
 */
static irq_handler_t ebbgpio_irq_handler1(unsigned int irq, void *dev_id, struct pt_regs *regs){
      led1On = !led1On;                          // Invert the LED state on each button press
      gpio_set_value(gpioLED1, led1On);          // Set the physical LED accordingly
      printk(KERN_INFO "GPIO_TEST: Interrupt 1 ! (button state is %d)\n", gpio_get_value(gpioButton1));
      numberPresses1++;                         // Global counter, will be outputted when the module is unloaded
      return (irq_handler_t) IRQ_HANDLED;      // Announce that the IRQ has been handled correctly
      
}

static irq_handler_t ebbgpio_irq_handler2(unsigned int irq, void *dev_id, struct pt_regs *regs){
   led2On = !led2On;                          // Invert the LED state on each button press
      gpio_set_value(gpioLED2, led2On);          // Set the physical LED accordingly
      printk(KERN_INFO "GPIO_TEST: Interrupt2 ! (button state is %d)\n", gpio_get_value(gpioButton2));
      numberPresses2++;                         // Global counter, will be outputted when the module is unloaded
      return (irq_handler_t) IRQ_HANDLED;      // Announce that the IRQ has been handled correctly
}

/// This next calls are  mandatory -- they identify the initialization function
/// and the cleanup function (as above).
module_init(ebbgpio_init);
module_exit(ebbgpio_exit);