# HW 02

## Buttons and LEDs

I performed the project for the buttons with the LEDs.  The file for this home work assignment is listed as [buttonsNstuff.py](https://github.com/Thebester5/Embeded-Linux/blob/master/hw02/buttonsNstuff.py "buttonsNstuff.py") . The GPIO pins for the assignment are as follows:
- LED1 : P9_16
- LED2 : P9_17
- LED3: P9_23
- LED4 : P9_24
- Button 1 : P9_11
- Button 2 : P9_12
- Button 3 : P9_13
- Button 4 : P9_14

## Measuring GPIO Pins with an Oscilliscope
The measured values and some observations were put down in TimingData.ods.

1. The min voltage was 3.3 V and the max voltage was 4.5 V.
2. The period was 137 ms.
3. The period was quite a ways off from 100 ms.
4. They differ due to the slow speeds at which bash scripts are interperated.
5. I was using 26% of my processor making that signal.
6. The shortest I could get the period to was 37 ms, which had 98% processor usage.
7. The period is very unstable.
8. Upon launching vi, the period of the signal became even more unstable.
9. I removed some lines I thought were unncessary, but due to my limited knowledge of shell files, did not make much of an inpact.
10. After swithing to sh and removing some uncooperative function calls, I was able to get a period fof 27.3 ms with a sleep cycle of .0005. This is a huge improvement over bash.
11. That was the shortest I could get in .sh files.  The shortest I got of all of them was C, where I was able to achieve a 117.8 us period in the signal.


## Etch A Sketch
The final portiion of this homework was improving on the etch a sketch program. I made this by extending the buttonsNLED python program and combining it with the game logic of the original etch a sketch program. This [file ](https://github.com/Thebester5/Embeded-Linux/blob/master/hw02/etchasketch.py "file ") utilizes these buttons for the commands:
- Left = P9_11
- Up = P9_12
- Down = P9_13
- Right= P9_14
- Clear = P9_21

Use these buttons to control the game board.

 
## Prof. Yoder's comments

Your table of times is missing.
etch-a-sketch looks good.

Grade:  8/10