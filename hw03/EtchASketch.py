#!/usr/bin/env python3

# Mark Procter
# ECE434
# Homework 2

import sys
import curses
import time
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
import smbus

bus = smbus.SMBus(2)
matrix = 0x70 # Use address

# rotary encoders
rotary_vert = RotaryEncoder(eQEP1)
rotary_horiz = RotaryEncoder(eQEP2)
rotary_vert.setAbsolute()
rotary_vert.enable()
rotary_horiz.setAbsolute()
rotary_horiz.enable()


# Start oscillator (p10)
bus.write_byte_data(matrix, 0x21, 0)
# Disp on, blink off (p11)
bus.write_byte_data(matrix, 0x81, 0)
# Full brightness (page 15)
bus.write_byte_data(matrix, 0xe7, 0)    
    
prev_vert_pos = rotary_vert.position
prev_horz_pos = rotary_horiz.position

cursor = [3, 3]
virtual = [[' '] * 8 for i in range(8)]
virtual[cursor[0]][cursor[1]] = '*'

while True:
    
    # led matrix var
    display = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    
    for y in range(8):
        for x in range(8):
            if y == cursor[0] and x == cursor[1]:
                display[2*x + 1] = display[2*x + 1] + pow(2, y)
            if virtual[y][x] == '*':
                display[2*x] = display[2*x] + pow(2, y)  
	
	
    bus.write_i2c_block_data(matrix, 0, display)
    
    vert_pos = rotary_vert.position
    horz_pos = rotary_horiz.position
    
    if vert_pos > prev_vert_pos: # up
        if cursor[1] < 7:
            cursor[1] += 1
        prev_vert_pos = vert_pos
        virtual[cursor[0]][cursor[1]] = '*'
    elif vert_pos < prev_vert_pos: # down
        if cursor[1]  > 0:
            cursor[1] -= 1
        prev_vert_pos = vert_pos
        virtual[cursor[0]][cursor[1]] = '*'

    # handle horizontal movement
    if horz_pos > prev_horz_pos: #right
        if cursor[0] > 0:
            cursor[0] -= 1
        prev_horz_pos = horz_pos
        virtual[cursor[0]][cursor[1]] = '*'
    elif horz_pos < prev_horz_pos: #left
        if cursor[0] < 7:
            cursor[0] += 1
        prev_horiz_pos = horz_pos
        virtual[cursor[0]][cursor[1]] = '*'
        
    time.sleep(0.1)
#end while


