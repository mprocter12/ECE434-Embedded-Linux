#! /bin/bash

# Mark Procter
# ECE434
# Homework 3


while true
do
    temp1=`i2cget -y 2 0x48`
    temp2=`i2cget -y 2 0x49`
    
    temp1F=$(($temp1*9/5+32))
    temp2F=$(($temp2*9/5+32))
    
    echo Temperature 1: $temp1F
    echo Temperature 2: $temp2F
    
    sleep 5
done