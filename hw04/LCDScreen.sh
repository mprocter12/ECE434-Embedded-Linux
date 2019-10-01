#! /bin/bash

# Mark Procter
# ECE434
# Homework 4

# Turn Display on
./on.sh

sleep 5

# Display image
sudo fbi -noverbose -T 1 -a boris.png

sleep 5

# Rotate screen
./rotate.sh

sleep 1

# Display Rotated Image
sudo fbi -noverbose -T 1 -a boris.png

sleep 5

sudo mplayer RedsNightmare.mpg

# Turn off Display 
./off.sh
