#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"


#define GPIO3_START_ADDR 0x481AE000
#define GPIOSET0 0x190
#define GPIOSET1 0x194
#define LED (1<<14) //GPIO3

unsigned int volatile * const GPIO3_CLEAR = (unsigned int *) (GPIO3_START_ADDR + GPIOSET0);
unsigned int volatile * const GPIO3_SET   = (unsigned int *) (GPIO3_START_ADDR + GPIOSET1);

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {
	int i;

	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	for(i=0; i<1000000000000; i++) {
		*GPIO3_SET   = LED;			// The the USR3 LED on

		__delay_cycles(0);    // Wait 1/2 second

		*GPIO3_CLEAR = LED;

		__delay_cycles(0); 

	}
	__halt();
}



