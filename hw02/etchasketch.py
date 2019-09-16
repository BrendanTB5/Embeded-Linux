#!/usr/bin/env python3
"""
Made by Brendan Mulholland
ECE 434- HW #2
"""

import Adafruit_BBIO.GPIO as GPIO
import time


left = "P9_11"
up = "P9_12"
down = "P9_13"
right= "P9_14"
clear = "P9_21"







def mycallback(channel):
    
    global playerX
    global playerY
    global board
    
    board[playerY][playerX] = 'X'
    
    
    if channel == up:
        playerY = playerY - 1
    elif channel == down:
        playerY = playerY + 1
    elif channel == left:
        playerX = playerX - 1
    elif channel == right:
        playerX += 1
    elif channel == clear:
        clearBoard("P9_10")
        
        
    board[playerY][playerX] = 'P'
    printer(board)


#This goes throguh the board and prints the lines and seperates them into rows corectly
def printer(grid):
    for row in grid:
        for e in row:
            print(e , end =" ")
        print()


def clearBoard(channel):
    global board
    global playerX
    global playerY
    n = 11
    m = 11
    board = [['-'] * m for i in range(n)]
    
    board[playerY][playerX] = 'P'
    printer(board)


def main():
    
   
    
    global playerX
    global playerY
    
   
    
    
   
    global board
    
    

    
    
    
    
    GPIO.setup(up, GPIO.IN)
    GPIO.setup(down, GPIO.IN)
    GPIO.setup(left, GPIO.IN)
    GPIO.setup(right, GPIO.IN)
    GPIO.setup(clear, GPIO.IN)
    
    GPIO.add_event_detect(left, GPIO.RISING,callback=mycallback, bouncetime=500)
    GPIO.add_event_detect(up, GPIO.RISING,callback=mycallback, bouncetime=500)
    GPIO.add_event_detect(down, GPIO.RISING,callback=mycallback, bouncetime=500)
    GPIO.add_event_detect(right, GPIO.RISING,callback=mycallback, bouncetime=500)
    GPIO.add_event_detect(clear, GPIO.RISING,callback=clearBoard, bouncetime=500)
        
   
    
    board[playerY][playerX] = 'P'
    
    printer(board)
    """
    
    while True:
        #The prevous locations
        board[playerY][playerX] = 'X'
    
        #This goes through the commands to apply the proper outcome to the commands
        com = input("Please Enter A Command: ")
        if com == "up":
            playerY = playerY - 1
        elif com == "down":
            playerY = playerY + 1
        elif com == "left":
            playerX = playerX - 1
        elif com == "right":
            playerX += 1
        elif com == "clear":
            board = [['-'] * m for i in range(n)]
     """       
        
            
    try:
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
    
            
    
    


if __name__ == "__main__":
    """ This is executed when run from the command line """
     #This is the size of the board and the init player location
    n = 11
    m = 11
    playerX = 6
    playerY = 6
    
     #This initialized the board to null and then adds the player's location
    board = [['-'] * m for i in range(n)]
    
    main()
