#!/usr/bin/env python3
"""
Made by Brendan Mulholland
ECE 434- HW #2
"""

import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import time
import smbus
from subprocess import call




def clearBoard():
    global red
    global green
    global board
    
    green = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    #red = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    
    board = [ [0] * 8 for _ in range(8)]
    
    displayBoard()
    
    
def displayBoard():
    
    global VertMatrix
    global green
    global red
    
    PosMatrix = [0x00,0x02,0x04,0x06,0x08,0x0A,0x0C,0x0E]
    
    green = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    
    for i in range(8):
        for j in range(8):
            green[i] += board[i][j] *  VertMatrix[j]
    
    for i in range(8):
        bus.write_i2c_block_data(matrix,PosMatrix[i],[green[i],red[i]])
    


def main():
    
   
    
    global playerX
    global playerY
    global board
    
   
    
    

    global encoder1
    global encoder2
        
   
 
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
            time.sleep(.5)
            global horiPos
            global vertPos
            global red
            global green
            global VertMatrix
            
            oldPlayerX = playerX
            oldPlayerY = playerY
            
            
            temp = bus.read_byte_data(address, 0)
            
            if(temp >= 26):
                clearBoard()
            
            
            
            
            
            
            #clearBoard("P9_10")
            
            
            if(encoder1.position < horiPos):
                playerX += 1
            elif(encoder1.position > horiPos):
                playerX += -1
            elif(encoder2.position < vertPos):
                playerY += 1
            elif(encoder2.position > vertPos):
                playerY += -1
            
            
            horiPos = encoder1.position
            vertPos = encoder2.position
            
            playerX = clamp(playerX,0,7)
            playerY = clamp(playerY,0,7)
            
            
            
            
            red[oldPlayerX] = red[oldPlayerX] - VertMatrix[oldPlayerY]
            red[playerX] = red[playerX] + VertMatrix[playerY]
            
            if(oldPlayerX != playerX or oldPlayerY != playerY):
                board[playerX][playerY] = 1
                
            
            displayBoard()
            
    except KeyboardInterrupt:
        GPIO.cleanup()
    
            
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
    


if __name__ == "__main__":
    """ This is executed when run from the command line """
     #This is the size of the board and the init player location
     
    
    #call("./configPin.sh")
    

    playerX = 4
    playerY = 4
    
    vertPos = 0
    horiPos = 0
    
    bus = smbus.SMBus(2)
    address = 0x48
    matrix = 0x70         # Use address 0x70
    
    bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
    bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
    bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)
    
    
    greenboard =  [ [0] * 8 for _ in range(8)]
    
    VertMatrix = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
    
    green = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    red = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    

    
     #This initialized the board to null and then adds the player's location
    clearBoard()
    encoder1 = RotaryEncoder(eQEP1)
    encoder2 = RotaryEncoder(eQEP2)
    encoder1.setAbsolute()
    encoder2.setAbsolute()
    encoder1.enable()
    encoder2.enable()
    
    red[playerX] = red[playerX] + VertMatrix[playerY]
    
    main()
