#!/usr/bin/env python3
"""
Made by Brendan Mulholland
ECE 434- HW #3
"""

from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import time
import smbus




def clearBoard():
    global board
    global playerX
    global playerY
    
    board = [ [0] * 8 for _ in range(8)]
    board[playerX][playerY] = 1
    
    displayBoard()
    
    
def displayBoard():
    
    global VertMatrix
    global red
    global matrix
    
    PosMatrix = [0x00,0x02,0x04,0x06,0x08,0x0A,0x0C,0x0E]
    
    green = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    
    for i in range(8):
        for j in range(8):
            green[i] += board[i][j] *  VertMatrix[j]
    
    for i in range(8):
        bus.write_i2c_block_data(matrix,PosMatrix[i],[green[i],red[i]])


            
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)    


def main():
    
    global playerX
    global playerY
    global board
    global encoder1
    global encoder2
    global red
    global VertMatrix
    
    vertPos = 0
    horiPos = 0
   
    while True:
        time.sleep(.5)
        
        
        oldPlayerX = playerX
        oldPlayerY = playerY
        
        
        temp = bus.read_byte_data(address, 0)
        
        if(temp >= 26):
            clearBoard()
        
        
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
            
    

    


if __name__ == "__main__":
    """ This is executed when run from the command line """
     #This is the size of the board and the init player location
     
    

    playerX = 4
    playerY = 4
    

    
    bus = smbus.SMBus(2)
    address = 0x48
    matrix = 0x70         # Use address 0x70
    
    bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
    bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
    bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)
    
    
    
   
    
    VertMatrix = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
    
    
    board = 0
    
    #green = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    red = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    
    
    #greenboard =  [ [0] * 8 for _ in range(8)]
    

    
     #This initialized the board to null and then adds the player's location
    clearBoard()
    
    #This sets up the encoders to zero
    encoder1 = RotaryEncoder(eQEP1)
    encoder2 = RotaryEncoder(eQEP2)
    encoder1.setAbsolute()
    encoder2.setAbsolute()
    encoder1.enable()
    encoder2.enable()
    
    red[playerX] = red[playerX] + VertMatrix[playerY]
    board[playerX][playerY] = 1
    
    main()
