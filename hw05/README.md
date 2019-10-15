# Home Work 5

Sorry about the wait for this. I didn't have my bone with me over break.

## Make

Make homework was completed successfully. It is available in the make folder.


## KernelModules Part 1

This is the first demo kernel module, for part 1 of the module section. It is run the same as the demo program.

## Kernel Modules Part 2

This is located in folder Part2. This module acts as a pipeline to transmit data passed to it and outputs it in dmesg.

## Kernel Modules Part 3

This runs the GPIO kernel module. I have 2 buttons hooked up to 3.3V and P8_15 and P8_18. These will be set to pullup by the kernel module. The module then toggles the button states to LEDs that are connected to P9_12 and P9_14. These LEDs are connected to the beaglebobne through a 330 Ohm resistor, and then to ground.

I have verified that this works, and both LEDs can be toggled at the same time.