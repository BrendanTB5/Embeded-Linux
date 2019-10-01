#!/bin/bash
#Brendan Mulholland
#ECE 434 Etch A Sketch Config


cd /sys/class/leds/beaglebone\:green\:usr3
echo none > trigger
echo 1 > brightness

cd /sys/class/leds/beaglebone\:green\:usr2
echo none > trigger
echo 1 > brightness


config-pin P8_07 in_pu
config-pin P8_26 in_pu

cd ~/Documents/Embeded-Linux/hw04

sudo ./mmapButton