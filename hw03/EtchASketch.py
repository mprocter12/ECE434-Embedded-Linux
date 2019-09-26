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

# led matrix var
display = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
displayEmpty = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]


# Start oscillator (p10)
bus.write_byte_data(matrix, 0x21, 0)
# Disp on, blink off (p11)
bus.write_byte_data(matrix, 0x81, 0)
# Full brightness (page 15)
bus.write_byte_data(matrix, 0xe7, 0)    
    
prev_vert_pos = rotary_vert.position
prev_horz_pos = rotary_horiz.position

cursor = [3, 3]
prevSpots = [[' '] * 8 for i in range(8)]
prevSpots[cursor[0]][cursor[1]] = '*'
try:
    while True:
    
        vert_pos = rotary_vert.position
        horz_pos = rotary_horiz.position
        
        if vert_pos > prev_vert_pos: # up
            if cursor[1] < 7:
                cursor[1] += 1
            prev_vert_pos = vert_pos
            prevSpots[cursor[0]][cursor[1]] = '*'
        elif vert_pos < prev_vert_pos: # down
            if cursor[1]  > 0:
                cursor[1] -= 1
            prev_vert_pos = vert_pos
            prevSpots[cursor[0]][cursor[1]] = '*'
        
        # handle horizontal movement
        if horz_pos > prev_horz_pos: #right
            if cursor[0] > 0:
                cursor[0] -= 1
            prev_horz_pos = horz_pos
            prevSpots[cursor[0]][cursor[1]] = '*'
        elif horz_pos < prev_horz_pos: #left
            if cursor[0] < 7:
                cursor[0] += 1
            prev_horiz_pos = horz_pos
            prevSpots[cursor[0]][cursor[1]] = '*'
            
            
        display[2*cursor[0]] = display[2*cursor[0]]|(0x80>>cursor[1])
        bus.write_i2c_block_data(matrix, 0, display)
            
        time.sleep(0.1)
    #end while

except KeyboardInterrupt:
    bus.write_i2c_block_data(matrix, 0, displayEmpty)





