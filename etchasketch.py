#!/usr/bin/env python3
"""
Made by Brendan Mulholland
ECE 434- HW #1
"""



def printer(grid):
    for row in grid:
        for e in row:
            print(e , end =" ")
        print()



def main():
    n = 11
    m = 11
    playerX = 6;
    playerY = 6;
    board = [["-"] * m for i in range(n)]
    board[playerY][playerX] = 'P'
    
    printer(board)

    
    while True:
        
        board[playerY][playerX] = 'X'
        
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
