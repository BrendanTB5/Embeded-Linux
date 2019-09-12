#!/usr/bin/env python3
"""
Made by Brendan Mulholland
ECE 434- HW #1
"""


#This goes throguh the board and prints the lines and seperates them into rows corectly
def printer(grid):
    for row in grid:
        for e in row:
            print(e , end =" ")
        print()



def main():
    #This is the size of the board and the init player location
    n = 11
    m = 11
    playerX = 6;
    playerY = 6;
    
    #This initialized the board to null and then adds the player's location
    board = [["-"] * m for i in range(n)]
    board[playerY][playerX] = 'P'
    
    printer(board)

    
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
            
        board[playerY][playerX] = 'P'
        
        
        
        printer(board)
            
        
            
    
    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
