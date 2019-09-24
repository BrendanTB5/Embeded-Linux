#!/usr/bin/env python3
# Gives us an alert when the TMP sensor goes high
# By: Brendan Mulholland

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4A

alertPin1 = 'P9_18'
alertPin2 = 'P9_15'

bus.write_byte_data(address1, 3, 0x1C)
bus.write_byte_data(address1, 2, 0x1B)
bus.write_byte_data(address1, 1, 0x84)
bus.write_byte_data(address2, 3, 0x1C)
bus.write_byte_data(address2, 2, 0x1B)
bus.write_byte_data(address2, 1, 0x84)



def callback1(channel):
    
    print("Alert 1 Triggered")
    while GPIO.input(alertPin1):
        temp = bus.read_byte_data(address1, 0)
        tempF = temp * 9 / 5 + 32
        print("Sensor 1: "+ str(tempF) + "F\r", end="")
        time.sleep(0.25)
    time.sleep(1)
    print("\n Alert Restored \n")
    
    
    
    
def callback2(channel):
    print("Alert 2 Triggered")
    while GPIO.input(alertPin2):
        temp = bus.read_byte_data(address2, 0)
        tempF = temp * 9 / 5 + 32
        print("Sensor 2: "+ str(tempF) + "F", end="\r")
        time.sleep(0.25)
    time.sleep(1)
    print("\n Alert Restored \n")
    
    
GPIO.setup(alertPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(alertPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(alertPin2, GPIO.BOTH, callback=callback2)
GPIO.add_event_detect(alertPin1, GPIO.BOTH, callback=callback1)    
    
try:
    while True:
        pass
            
except KeyboardInterrupt:
        bus.write_byte_data(address1, 3, 0x00)
        bus.write_byte_data(address1, 2, 0x00)
        bus.write_byte_data(address1, 1, 0x00)
        bus.write_byte_data(address2, 3, 0x00)
        bus.write_byte_data(address2, 2, 0x00)
        bus.write_byte_data(address2, 1, 0x00)
        GPIO.cleanup()
