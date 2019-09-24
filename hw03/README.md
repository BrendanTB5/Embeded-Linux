# Home Work 3


### Files
- [alertTemp.py](https://github.com/Thebester5/Embeded-Linux/blob/master/hw03/alertTemp.py "alertTemp.py")
- [configPin.sh](https://github.com/Thebester5/Embeded-Linux/blob/master/hw03/configPin.sh "configPin.sh")
- [etchasketch.py](https://github.com/Thebester5/Embeded-Linux/blob/master/hw03/etchasketch.py "etchasketch.py")
- [tempRead.sh](https://github.com/Thebester5/Embeded-Linux/blob/master/hw03/tempRead.sh " tempRead.sh")


## Setup

To setup the pins for this homework, run configPin.sh before running any of the other files.

## Problem 1

For problem one I utalized two TMP101 sensors, one on I2C Bus at address 0x48 and the other at address 0x4A. Running tempRead.sh will return the values of the sensors in degrees Fahrenheit. 
Running the program alertTemp.py will only read the temperature of a sensor when the temperature goes above 28C, and will stop reading the temperature when it goes below 27C.

## Problem 2 & 3

For problems two and three the etchasketch.py program is used. The program is designed to interface with an 8x8 display at address 0x70. To move around the board, you have to use two encoders located at P8-11  P8-12 ;and  P8-33  P8-35. I also used a TMP101 sensor at address 0x48 as a clear sensor, with the sensor going off when the temperature goes above 26 degrees.
