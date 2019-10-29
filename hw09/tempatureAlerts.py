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
        tempC0 = bus.read_byte_data(tempSensors[0], 0)
        tempF0 = tempC0*(9/5)+32
        print('Temperature alarm triggered at: ' + str(tempF0) + ' degrees Fahrenheit')
        
    if(GPIO.input(ALRM[0])):
        print('Temparture alarm returned to normal')
        
    if(alert==ALRM[1]):
        tempC1 = bus.read_byte_data(tempSensors[1], 0)
        tempF1 = tempC1*(9/5)+32
        print('Temperature alarm triggered at: ' + str(tempF1) + ' degrees Fahrenhei')
        
    if(GPIO.input(ALRM[1])):
        print('Temparture alarm returned to normal')
        
        


# temp sensor setup
bus = smbus.SMBus(2)
tempSensors = [0x48, 0x49]
alarmTemp = 28
ALRM = ["P9_11", "P9_12"]

for alarm in ALRM:
    GPIO.setup(alarm, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(alarm, GPIO.BOTH, callback=handleTempAlarm)
    
for address in tempSensors:
    bus.write_byte_data(address, 3, 25)
    bus.write_byte_data(address, 2, 24)

while True:
    pass
