
from lib_tft24T import TFT24T
import Adafruit_BBIO.GPIO as GPIO

import spidev
from time import sleep

# Raspberry Pi configuration.
PEN = "P9_15"

TFT = TFT24T(spidev.SpiDev(), GPIO)
# Raw touch output is intrinsically portrait mode

TFT.initTOUCH(PEN)

while 1:
    while not TFT.penDown():
        pass

    print("%03X" % TFT.readValue(TFT.X))
    print("%03X" % TFT.readValue(TFT.Y))

    print("")
    sleep(.5)
