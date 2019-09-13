#!/usr/bin/env python3

# Mark Procter
# ECE434
# Homework 2

import Adafruit_BBIO.GPIO as GPIO

toggs = "GP9_14"

GPIO.setup(LED, GPIO.OUT)

while 1:
    GPIO.output(toggs, 1)
    GPIO.output(toggs, 0)

    