#!/usr/bin/env python3

# Mark Procter
# ECE434
# Homework 2

import sys
import curses
import time
import Adafruit_BBIO.GPIO as GPIO


def shake(height, width, stdscr, blankChar):

    stdscr.clear()

    # fill screen
    for y in range(0,height):
        for x in range(0, width):
            try:
                stdscr.addstr(y,x,blankChar)
            except curses.error:
                print("The size of the window selected is too small for the current terminal, please enlarge terminal and try again")
            #end for x
        #end for y


def main(stdscr, height, width):

    # global goLeft, goRight, goUp, goDown
    
    position = [0,0]
    blankChar = "8"
    drawnChar = " "
    cursor = "*"
    stdscr = curses.initscr()
    prevSpots = list(position)

    #set the screen up
    shake(height, width, stdscr, blankChar)

    while True:
        stdscr.addstr(position[1], position[0], cursor)
        if GPIO.input(btn1) and GPIO.input(btn2):
            break
        elif GPIO.input(btn3) and GPIO.input(btn4):
            shake(height, width, stdscr,blankChar)
            prevSpots = list(position)
            continue
        elif GPIO.input(btn1):
            if(position[1] > 0):
                position[1] -= 1
        elif GPIO.input(btn2):
            if(position[1] < height -1):
                position[1] += 1
        elif GPIO.input(btn3):
            if(position[0] > 0):
                position[0] -= 1
        elif GPIO.input(btn4):
            if(position[0] < width -1):
                position[0] += 1
        

        stdscr.addstr(prevSpots[1], prevSpots[0], drawnChar)
        prevSpots = list(position)
        stdscr.refresh()
        time.sleep(0.1)
    #end while

#end main

btn1 = "P9_11"
btn2 = "P9_12"
btn3 = "P9_13"
btn4 = "P9_14"

GPIO.setup(btn1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(btn2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(btn3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(btn4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

print("The following describe the instructions to play Etch-A-Sketch: " +
    "To draw on the screen use your arrow keys, the cursor will appear as a *. " +
    "Use 's' to shake the screen and 'q' to quit")

    
height = input("Set screen height: ")
width =  input("Set screen width: ")
curses.wrapper(main, int(height), int(width))


