#!/usr/bin/env python3
# Gives us an alert when the TMP sensor goes high
# By: Brendan Mulholland

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4A

alertPin1 = 'P9_15'
alertPin2 = 'P9_18'

bus.write_byte_data(address1, 3, 28)
bus.write_byte_data(address1, 2, 27)
bus.write_byte_data(address2, 3, 28)
bus.write_byte_data(address2, 2, 27)



def callback1(channel):
    
    print("Alert 2 Triggered")
    while GPIO.input(alertPin1):
        temp = bus.read_byte_data(address1, 0)
        tempF = temp * 5 / 9 + 32
        print("Sensor 1: "+ str(temp) + "F\r", end="")
        time.sleep(0.25)
    print("\n Alert Restored \n")
    
    
    
    
def callback2(channel):
    print("Alert 1 Triggered")
    while GPIO.input(alertPin1):
        temp = bus.read_byte_data(address1, 0)
        tempF = temp * 5 / 9 + 32
        print("Sensor 2: "+ str(temp) + "F\r", end="")
        time.sleep(0.25)
    print("\n Alert Restored \n")
    
GPIO.setup(alertPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(alertPin1, GPIO.RISING, callback=callback1)
GPIO.setup(alertPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(alertPin2, GPIO.RISING, callback=callback2)    
    
try:
    while True:
            time.sleep(.5)
            
except KeyboardInterrupt:
        GPIO.cleanup()
