#!/usr/bin/env python3
"""
Made by Brendan Mulholland
ECE 434- HW #2
"""

import Adafruit_BBIO.GPIO as GPIO
import time


B1 = "P9_11"
B2 = "P9_12"
B3 = "P9_13"
B4 = "P9_14"

L1 = "P9_16"
L2 = "P9_17"
L3 = "P9_23"
L4 = "P9_24"


def mycallback(channel):
    if(GPIO.input(channel)):
        if channel == B1:
            GPIO.output(L1, GPIO.HIGH)
        elif channel == B2:
            GPIO.output(L2, GPIO.HIGH)
        elif channel == B3:
            GPIO.output(L3, GPIO.HIGH)
        elif channel == B4:
            GPIO.output(L4, GPIO.HIGH)
    else:
        if channel == B1:
            GPIO.output(L1, GPIO.LOW)
        elif channel == B2:
            GPIO.output(L2, GPIO.LOW)
        elif channel == B3:
            GPIO.output(L3, GPIO.LOW)
        elif channel == B4:
            GPIO.output(L4, GPIO.LOW)
          
          

def main():
   
    
    
    GPIO.setup(B1, GPIO.IN)
    GPIO.setup(B2, GPIO.IN)
    GPIO.setup(B3, GPIO.IN)
    GPIO.setup(B4, GPIO.IN)
    
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(L3, GPIO.OUT)
    GPIO.setup(L4, GPIO.OUT)
    
    GPIO.add_event_detect(B1, GPIO.BOTH,callback=mycallback)
    GPIO.add_event_detect(B2, GPIO.BOTH,callback=mycallback)
    GPIO.add_event_detect(B3, GPIO.BOTH,callback=mycallback)
    GPIO.add_event_detect(B4, GPIO.BOTH,callback=mycallback)
    
    try:
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
    
    








if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
