# File:          proj2.py
# Author:        Kai Vilbig
# Date:          11/5/2018
# Section:       28
# E-mail:        sw92057@umbc.edu
# Description:   connecct 4 game

from random import randint

QUIT = "n"
PLAY_AGAIN = "y"
PLAYER1_MARK = "X"
PLAYER2_MARK = "O"
BLANK_SPACE = "_"
MIN_WIDTH = 5
MIN_HEIGHT = 5

# ------------------------------------------------------------

# Builds the board
def boardBuild(width, height, board):

    for i in range(height):

        row = []
        for j in range(width):

            row.append(BLANK_SPACE)
            print(row[j], end=" ")

        print()
        board.append(row)

    print()

# ------------------------------------------------------------

# checks if the player who just went won
def checkWin(player_mark, width, height, board):

    win = False

    # check row for win
    # add height + 1 and width - 3 because you can not start
    # a 4 in a row from 3 away from the edge. therefor, by
    # putting the numbers in as I did, it will only check
    # up till the 4th index from the end. This will apply
    # to all the other checks later in the code.
    for i in range(height + 1):

        for j in range(width - 3):

            # makes sure to stop checking once you win
            if win != True:
                            
                if board[i][j] == player_mark and \
                     board[i][j + 1] == player_mark and \
                     board[i][j + 2] == player_mark and \
                     board[i][j + 3] == player_mark:

                    win = True

    # will only check column if row didnt fin 4 in a row
    if win != True:
        
        # check column for win
        for i in range(height - 2):

            for j in range(width):

                # makes sure to stop checking once you win
                if win != True:

                    if board[i][j] == player_mark and \
                         board[i + 1][j] == player_mark and \
                         board[i + 2][j] == player_mark and \
                         board[i + 3][j] == player_mark:

                        win = True

    # will only check diagnal down if row and column didnt find
    # 4 in a row
    if win != True:

        for i in range(height - 2):

            for j in range(width - 3):

                # makes sure to stop checking once you win
                if win != True:

                    if board[i][j] == player_mark and \
                         board[i + 1][j + 1] == player_mark and \
                         board[i + 2][j + 2] == player_mark and \
                         board[i + 3][j + 3] == player_mark:

                        win = True

    # will only check diagnal up if all other checks havent
    # found 4 in a row
    if win != True:

        # start i at 3 because there can not be 4 in a row diagnally
        # up starting at the third from the top space
        for i in range(3, height + 1):

            for j in range(width - 3):

                # makes sure to stop checking once you win
                if win != True:

                    if board[i][j] == player_mark and \
                         board[i - 1][j + 1] == player_mark and \
                         board[i - 2][j + 2] == player_mark and \
                         board[i - 3][j + 3] == player_mark:

                        win = True
                        
    if win != True:

        if BLANK_SPACE not in board[0]:

            win = "Draw"

    return win
# ------------------------------------------------------------

# prints the board after player has put a mark in a column
def printBoard(board, width):

    for i in range(len(board)):

        for j in range(width):

            print(board[i][j], end=" ")

        print()

    print()
            
# -----------------------------------------------------------

# checks columns and updates board based on player mark
def columnCheck(board, column, height, player_mark):

    # if the character in the index of the column is _, change
    # it to the player's mark. To do this, start at the
    # bottom of the column
    if board[height][column] == BLANK_SPACE:

        board[height][column] = player_mark

    # recursive. keep calling the function until the right
    # height is found and the program changes _ to the
    # player's mark
    else:

        columnCheck(board, column, height - 1, player_mark)

# -----------------------------------------------------------

# plays the game
def play(comp, board, width, height):

    win = False
    while win != True and win != "Draw":

        print("Player 1 what is your choice?")
        column = int(input("Enter a column to place your " \
                           "piece in (1 - " + str(width) + "): ")) - 1

        # makes sure user does not enter column under 1 or
        # over the width
        while column < 0 or column > width - 1:

            print("please chose a valid column")
            print()
            column = int(input("Enter a column to place your " \
                           "piece in (1 - " + str(width) + "): ")) - 1

        # checks to make sure the column is not full
        while board[0][column] != BLANK_SPACE:

            print("That Column is full. Chose a different " \
                  "column")
            print()
            column = int(input("Enter a column to place your " \
                               "piece in (1 - " + str(width) + "): ")) - 1

            # makes sure user does not enter column under 1 or
            # over the width
            while column < 0 or column > width - 1:

                print("please chose a valid column")
                print()
                column = int(input("Enter a column to place your " \
                                   "piece in (1 - " + str(width) + "): ")) - 1
                    
        columnCheck(board, column, height, PLAYER1_MARK)
        printBoard(board, width)
        win = checkWin(PLAYER1_MARK, width, height, board)

        if win == True:

            print("Player 1 wins!")

        elif win == "Draw":

            print("It's a draw!")
            
        # if player 1 wins, player two will not be able to do
        # their turn
        if win != True and win != "Draw":
            if comp == "y":

                print("It's the computer's turn")
                column = randint(0, width - 1)
                print("the computer chose", column + 1)

            else:

                print("Player 2 what is your choice?")
                column = int(input("Enter a column to place your " \
                                   "piece in (1 - " + str(width) + "): ")) - 1

                # makes sure user does not enter column under 1 or
                # over the width
                while column < 0 or column > width - 1:

                    print("please chose a valid column")
                    print()
                    column = int(input("Enter a column to place your " \
                                   "piece in (1 - " + str(width) + "): ")) - 1

                # checks to make sure the column is not full
                while board[0][column] != BLANK_SPACE:

                    print("That Column is full. Chose a different " \
                          "column")
                    print()
                    column = int(input("Enter a column to place your " \
                                       "piece in (1 - " + str(width) + "): ")) - 1

                    # makes sure user does not enter column under 1 or
                    # over the width
                    while column < 0 or column > width - 1:

                        print("please chose a valid column")
                        print()
                        column = int(input("Enter a column to place your " \
                                           "piece in (1 - " + str(width) + "): ")) - 1

            columnCheck(board, column, height, PLAYER2_MARK)
            printBoard(board, width)
            win = checkWin(PLAYER2_MARK, width, height, board)

            if win == True:

                print("Player 2 Wins!")

            elif win == "Draw":

                print("It's a draw!")
                
    return True
    
# -----------------------------------------------------------

def main():

    print()

    quitGame = False
    while quitGame != QUIT:

        board = []
        height = int(input("Enter a height: "))

        # makes sure board is atleast 5 spaces high
        while height < MIN_HEIGHT:

            print("Height has to be 5 or bigger")
            height = int(input("Enter a height: "))
        width = int(input("Enter a width: "))

        # makes sure board is atleast 5 spaces wide
        while width < MIN_WIDTH:

            print("Width has to be 5 or bigger")
            width = int(input("Enter a width: "))

        # decides single player or multiplayer
        comp = input("Play against the Computer? (y/n): ")

        boardBuild(width, height, board)
        
        play(comp, board, width, height - 1)

        quitGame = input("Would you like to play again? (y/n): ")

        while quitGame != QUIT and quitGame != PLAY_AGAIN:

            print()
            print("Please chose \"y\" or \"n\"")
            quitGame = input("Would you like to play again? (y/n): ")
            
        print()
       
main()
