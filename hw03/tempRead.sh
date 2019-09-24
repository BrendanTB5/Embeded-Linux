#!/bin/bash
#Brendan Mulholland
#ECE 434 Temp Get

temp=$(i2cget -y 2 0x48)

temp2=$(i2cget -y 2 0x4a)

temp1F=$(( (($temp * 5) / 9) + 32 ))
temp2F=$(( (($temp2 * 5) / 9) + 32 ))

echo $temp1F
echo $temp2F