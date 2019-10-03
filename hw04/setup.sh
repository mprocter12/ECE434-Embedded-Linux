#!/bin/sh

cd /sys/class/leds/beaglebone\:green\:usr2
echo none > trigger
echo 0 > brightness

cd /sys/class/leds/beaglebone\:green\:usr3
echo none > trigger
echo 0 > brightness