#!/usr/bin/env python3

# Mark Procter
# ECE434
# Homework 2


import Adafruit_BBIO.GPIO as GPIO


# Setup variables for the buttons and LEDS
btn1 = "P9_11"
btn2 = "P9_13"
btn3 = "P9_15"
btn4 = "P9_17"
led1 = "P9_19"
led2 = "P9_20"
led3 = "P9_21"
led4 = "P9_22"

buttons2LEDS = {btn1: led1, btn2: led2, btn3: led3, btn4: led4}

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(btn1, GPIO.IN)
GPIO.setup(btn2, GPIO.IN)
GPIO.setup(btn3, GPIO.IN)
GPIO.setup(btn4, GPIO.IN)

def turnOnLED(button):
    state = GPIO.input(button)
    GPIO.output(map[button], state)

# Turn LEDs off
GPIO.output(led1, 0)
GPIO.output(led2, 0)
GPIO.output(led3, 0)
GPIO.output(led4, 0)

GPIO.add_event_detect(btn1, GPIO.BOTH, callback=turnOnLED)
GPIO.add_event_detect(btn2, GPIO.BOTH, callback=turnOnLED)
GPIO.add_event_detect(btn3, GPIO.BOTH, callback=turnOnLED)
GPIO.add_event_detect(btn4, GPIO.BOTH, callback=turnOnLED)

try:
    while 1:
        continue
except KeyboardInterrupt:
    GPIO.cleanup()
