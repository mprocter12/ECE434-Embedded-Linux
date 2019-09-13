#!/usr/bin/env python3

# Mark Procter
# ECE434
# Homework 2

import Adafruit_BBIO.GPIO as GPIO

toggs = "P9_14"

GPIO.setup(toggs, GPIO.OUT)

while 1:
    GPIO.output(toggs, GPIO.HIGH)
    GPIO.output(toggs, GPIO.LOW)

    
