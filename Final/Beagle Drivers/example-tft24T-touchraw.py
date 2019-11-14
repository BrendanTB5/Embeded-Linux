#!/usr/bin/env python3
from lib_tft24T import TFT24T
import Adafruit_BBIO.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

from Adafruit_BBIO.SPI import SPI
from time import sleep

#DC = "P9_15"
RST = "P9_14"
LED = "P9_26"
PEN = "P9_15"

TFT = TFT24T(SPI, GPIO, landscape=False)
# Raw touch output is intrinsically portrait mode

TFT.initTOUCH(PEN)

while 1:
    while not TFT.penDown():
        pass

    print("%03X" % TFT.readValue(TFT.X))
    print("%03X" % TFT.readValue(TFT.Y))

    print("")
    sleep(.5)
