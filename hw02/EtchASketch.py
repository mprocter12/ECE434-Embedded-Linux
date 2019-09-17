#!/usr/bin/env python3

# Mark Procter
# ECE434
# Homework 2

import sys
import curses
import time
import Adafruit_BBIO as GPIO


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

def leftButton(channel):
    global goLeft
    state = GPIO.input(channel)
    goLeft = state

def rightButton(channel):
    global goRight
    state = GPIO.input(channel)
    goRight = state

def upButton(channel):
    global goUp
    state = GPIO.input(channel)
    goUp = state

def downButton(channel):
    global goDown
    state = GPIO.input(channel)
    goDown = state


def main(stdscr, height, width):

    global goLeft, goRight, goUp, goDown
    
    position = [0,0]
    blankChar = "8"
    drawnChar = " "
    cursor = "*"
    stdscr = curses.initscr()
    prevSpots = list(position)
    btn1 = "P9_16"
    btn2 = "P9_18"
    btn3 = "P9_15"
    btn4 = "P9_17"

    GPIO.setup(btn1, GPIO.IN)
    GPIO.setup(btn2, GPIO.IN)
    GPIO.setup(btn3, GPIO.IN)
    GPIO.setup(btn4, GPIO.IN)

    GPIO.add_event_detect(btn1, GPIO.BOTH, callback=upButton)
    GPIO.add_event_detect(btn2, GPIO.BOTH, callback=downButton)
    GPIO.add_event_detect(btn3, GPIO.BOTH, callback=leftButton)
    GPIO.add_event_detect(btn4, GPIO.BOTH, callback=rightButton)

    #set the screen up
    shake(height, width, stdscr, blankChar)

    while True:
        stdscr.addstr(position[1], position[0], cursor)
        curse = stdscr.getch(height-1, width-1)
        if goUp == 1:
            if(position[1] > 0):
                position[1] -= 1
        elif goDown == 1:
            if(position[1] < height -1):
                position[1] += 1
        elif goLeft == 1:
            if(position[0] > 0):
                position[0] -= 1
        elif goRight == 1:
            if(position[0] < width -1):
                position[0] += 1
        elif curse == ord('q'):
            break
        elif curse == ord('s'):
            shake(height, width, stdscr,blankChar)
            prevSpots = list(position)
            continue

        stdscr.addstr(prevSpots[1], prevSpots[0], drawnChar)
        prevSpots = list(position)
    #end while

#end main


goDown = 0
goLeft = 0
goUp = 0
goRight = 0

print("The following describe the instructions to play Etch-A-Sketch: " +
    "To draw on the screen use your arrow keys, the cursor will appear as a *. " +
    "Use 's' to shake the screen and 'q' to quit")

    
height = input("Set screen height: ")
width =  input("Set screen width: ")
curses.wrapper(main, int(height), int(width))


