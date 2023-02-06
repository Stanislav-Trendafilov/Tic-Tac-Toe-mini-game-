'''
Students names and class number
The current year
Here goes the code description
'''
import random as r
import sys
import colorama
from colorama import Fore

def newBoard():
    """
    Generates an empty 3x3 board in two dimensional array.
    """
    return [[0, 0, 0] for i in range(3)]

def saveGame(filename, game):
    '''
	Saves the current game to a file.
    '''
    try:
        with open(f"{filename}.txt", "w") as f:
            f.write(str(game))
    except:
        print("Couldn't save the game. Exiting now.")

def loadGame(filename):
    '''
	Loads a saved game from a file.
    '''
    try:
        with open(f"{filename}.txt", "r") as f:
            game = eval(f.read())
        return game
    except:
        print("File with that name hasn't been found!")
        return None


def printBoard(board):
    '''
    Checking the value of all cells and print X or 0 in different colours.
    Check if the element is last for the line in order to print new line.
    '''
    for i in board:
        br = 0
        for j in i:
            if br != 2:
                if j == 0:
                    print(" |", end="")
                elif j == 1:
                    print(Fore.RED + "0" + Fore.RESET + "|", end="")
                elif j == 2:
                    print(Fore.BLUE + "X" + Fore.RESET + "|", end="")
                br = br+1
            else:
                if j == 0:
                    print(" ")
                elif j == 1:
                    print(Fore.RED + "0"+Fore.RESET)
                elif j == 2:
                    print(Fore.BLUE + "X"+Fore.RESET)

def makeMove(row, column, board):
    '''
	Set a cell value for the player. We subtract 1 from the column and row value because the numbering starts from 0.
    '''
    board[row-1][column-1] = 1
    printBoard(board)

def validMove(row, column, board):
    '''
	Checking if the values of row and column are valid(between 0 and 3) and if this cell is empty.
	Returns True or False.
    '''
    is_valid = True
    if row > 3 or row < 0 or column > 3 or column < 0:
        is_valid = False
    elif board[row-1][column-1] != 0:
        is_valid = False
    return is_valid

def checkWinnerV(turn, board):
    '''
	Check the values of the 3 columns and returns True or False.
    '''
    is_valid = False
    if board[0][0] == board[1][0] == board[2][0] == turn:
        is_valid = True
    elif board[0][1] == board[1][1] == board[2][1] == turn:
        is_valid = True
    elif board[0][2] == board[1][2] == board[2][2] == turn:
        is_valid = True
    return is_valid

def checkWinnerH(turn, board):
    '''
	Check the values of the 3 rows and returns True or False.
    '''
    is_valid = False
    if board[0][0] == board[0][1] == board[0][2] == turn:
        is_valid = True
    elif board[1][0] == board[1][1] == board[1][2] == turn:
        is_valid = True
    elif board[2][0] == board[2][1] == board[2][2] == turn:
        is_valid = True
    return is_valid

def checkWinnerD(turn, board):
    '''
	Check the values of the 2 diagonals and returns True or False.
    '''
    is_valid = False
    if board[0][2] == board[1][1] == board[2][0] == turn:
        is_valid = True
    elif board[0][0] == board[1][1] == board[2][2] == turn:
        is_valid = True
    return is_valid

def checkWinner(turn, board):
    '''
	Checks if the current player has column,row or diagonal with the previous functions.
    '''
    is_winner = False
    if checkWinnerV(turn,board) == True or checkWinnerH(turn,board) == True or checkWinnerD(turn,board) == True:
        is_winner = True
    return is_winner

def computerMove(board):
    '''
	Making computer movement with random class and checking the values with validMove function.
    '''
    row = r.randint(1, 3)
    column = r.randint(1, 3)
    while validMove(row,column,board) != True:
        row = r.randint(1, 3)
        column = r.randint(1, 3)

    board[row-1][column-1] = 2
    printBoard(board)

def checkFull(board):
    '''
	Check if the board is full(if the cell is not equal to 0)
    '''
    is_full = True
    for i in board:
        for j in i:
            if j == 0:
                is_full = False
    return is_full

if __name__ == "__main__":
      print("Welcome to the game. Choose your option from the listed below:")
      board = newBoard()

      print("Press (n) ew game / (l) oad game")
      answer = input()
      while answer != "n" and answer != "l":
        print("You should write letter between n(new game) and l(load game)")
        answer=input()
      if answer == "n":
          nickname=input("Enter your nickname: ")
          game = {"nickname": nickname, "turn": 1, "board": board}
          print("To make a move, enter row and column numbers (from 1 to 3). To save the game, enter ‘s’ for a row.")
      elif answer == 'l':
          load_game=input("Enter the name of your load game: ")
          game=loadGame(load_game)
          printBoard(game["board"])

      while checkFull(board) == False:
        turn = 1
        print("Your turn")
        print("Please enter the number of the row:")
        row = input()
        while row != "s" and row != "1" and row != "2" and row != "3":
            print("Please enter the number of the row between 1 and 3")
            row = input()
        if row == 's':
            filename = input("Enter filename: ")
            saveGame(filename, game)
            break
        else:
            row = int(row)
        print("Please enter the number of the column:")

        column = input()
        while column != "1" and column != "2" and column != "3":
            print("Please enter the number of the column between 1 and 3")
            column = input()
        column = int(column)

        while validMove(int(row),int(column),game["board"]) != True:
            print("Invalid input!!!!")
            print("Please enter the number of the row:")
            row = input()
            while row != "s" and row != "1" and row != "2" and row != "3":
                print("Please enter the number of the row between 1 and 3")
                row = input()
            if row == 's':
                filename = input("Please enter name of the file:")
                saveGame(filename, game)
                break
            print("Please enter the number of the column:")
            column = input()
            while column != "1" and column != "2" and column != "3":
                print("Please enter the number of the column between 1 and 3")
                column = input()

        makeMove(int(row),int(column), game["board"])
        if checkWinner(turn,game["board"])==True:
            print("You won! Congratulations")
            break
        elif checkFull(game["board"])==True:
            print("The game is а draw!")


        print("Computer is thinking....")
        turn = 2
        computerMove(game["board"])
        game = {"nickname": game["nickname"], "turn": 1, "board": game["board"]}
        if checkWinner(turn, game["board"]) == True:
            print("You lost! Maybe next time...")
            break
        elif checkFull(game["board"])==True:
            print("The game is а draw!")


