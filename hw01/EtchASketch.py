#!/usr/bin/env python3

# Mark Procter
# ECE434
# Homework 1

import sys
import curses
import time


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
        curse = stdscr.getch(height-1, width-1)
        if curse == curses.KEY_UP:
            if(position[1] > 0):
                position[1] -= 1
        elif curse == curses.KEY_DOWN:
            if(position[1] < height -1):
                position[1] += 1
        elif curse == curses.KEY_LEFT:
            if(position[0] > 0):
                position[0] -= 1
        elif curse == curses.KEY_RIGHT:
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


print("The following describe the instructions to play Etch-A-Sketch: " +
    "To draw on the screen use your arrow keys, the cursor will appear as a *. " +
    "Use 's' to shake the screen and 'q' to quit")

    
height = input("Set screen height: ")
width =  input("Set screen width: ")
curses.wrapper(main, int(height), int(width))


