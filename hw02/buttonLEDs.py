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
LED1 = "P9_19"
LED2 = "P9_20"
LED3 = "P9_21"
LED4 = "P9_22"

buttons2LEDS = {btn1: LED1, btn2: LED2, btn3: LED3, btn4: LED4}

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(btn1, GPIO.IN)
GPIO.setup(btn2, GPIO.IN)
GPIO.setup(btn3, GPIO.IN)
GPIO.setup(btn4, GPIO.IN)

def turnOnLED(button):
    state = GPIO.input(button)
    GPIO.output(map[button], state)

# Turn LEDs off
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(LED4, 0)

GPIO.add_event_detect(btn1, GPIO.BOTH, callback=turnOnLED)
GPIO.add_event_detect(btn2, GPIO.BOTH, callback=turnOnLED)
GPIO.add_event_detect(btn3, GPIO.BOTH, callback=turnOnLED)
GPIO.add_event_detect(btn4, GPIO.BOTH, callback=turnOnLED)

try:
    while 1:
        continue
except KeyboardInterrupt:
    GPIO.cleanup()
