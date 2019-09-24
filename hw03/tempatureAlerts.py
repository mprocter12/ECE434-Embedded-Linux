#!/usr/bin/env python3

# Mark Procter
# ECE434
# Homework 3

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time

def handleTempAlarm(alert):
    print("Alert Signal Received")
    if(alert==ALRM[0]):
        print('Temperature alarm triggered at: ' + str(bus.read_byte_data(tempSensors[0], 0)))
    if(alert==ALRM[1]):
        print('Temperature alarm triggered at: ' + str(bus.read_byte_data(tempSensors[1], 0)))


# temp sensor setup
bus = smbus.SMBus(2)
tempSensors = [0x48, 0x49]
alarmTemp = 28
ALRM = ["P9_11", "P9_12"]

for alarm in ALRM:
    GPIO.setup(alarm, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(alarm, GPIO.BOTH, callback=handleTempAlarm)
    
for address in tempSensors:
    bus.write_byte_data(address, 3, 26)
    bus.write_byte_data(address, 2, 24)

while True:
    pass
