# Home Work 4


### Files
- [mmapButton.c](https://github.com/Thebester5/Embeded-Linux/blob/master/hw04/mmapButton.c "mmapButton.c")
- [mmapFast.c](https://github.com/Thebester5/Embeded-Linux/blob/master/hw04/mmapFast.c "mmapFast.c")

## Memory Map

![Memory Map With GPIO and SDRAM](https://github.com/Thebester5/Embeded-Linux/blob/master/hw04/Map.jpg?raw=true "Memory Map With GPIO and SDRAM")


## Buttons And LEDS

Please run configPinButtons.sh before running this file. The buttons are connected to P8_7 and P8_26. The buttons are connected to ground, and activate user leds 2 and 3.

## Fast MMAP

Here the MMAP is able to toggle the GPIO pin at a rate of about 9.71 MHz. This frequency lead to the signal barely having time to settle from oscillations. This program outputs on P8_26. Please run configPinFast.sh before running this program.

## Images from the Display Test
![Borris Normal](https://github.com/Thebester5/Embeded-Linux/blob/master/hw04/Borris.jpg?raw=true "Borris Normal")

![Borris Rotated](https://github.com/Thebester5/Embeded-Linux/blob/master/hw04/BorrisRotate.jpg?raw=true "Borris Rotate")

![Video Rotated](https://github.com/Thebester5/Embeded-Linux/blob/master/hw04/VideoRotate.jpg?raw=true "Video Rotate")

![Display Text](https://github.com/Thebester5/Embeded-Linux/blob/master/hw04/Text.jpg?raw=true "My Name")

## Prof. Yoder's comments

Very good.  Nice pictures.

Grade:  10/10