# Sudoku solver by Jordin Myers
# solving steps are based on this wikipedia article https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#/media/File:Sudoku_solved_by_bactracking.gif

from time import sleep as sleep
from pynput import keyboard # pip install pynput
from pynput.keyboard import Key
from datetime import datetime
import os

#set up board
boardData = { # creates a 9x9 board with all values set to "." - backend use
    i: ["."]*9 for i in range(9)
}
pos = [0,0] # starting position
solved = False # used to check if the board is solved
message = """ 
Use the arrow keys to move the cursor and the number keys to enter a number.
Press esc to exit.
Press enter to submit.
""" # instructions

#functions
def create_board(): # creates the board that will be displayed to user
    b = f"""
        -------------------------
        | {boardData[0][0]} {boardData[0][1]} {boardData[0][2]} | {boardData[0][3]} {boardData[0][4]} {boardData[0][5]} | {boardData[0][6]} {boardData[0][7]} {boardData[0][8]} |
        | {boardData[1][0]} {boardData[1][1]} {boardData[1][2]} | {boardData[1][3]} {boardData[1][4]} {boardData[1][5]} | {boardData[1][6]} {boardData[1][7]} {boardData[1][8]} |
        | {boardData[2][0]} {boardData[2][1]} {boardData[2][2]} | {boardData[2][3]} {boardData[2][4]} {boardData[2][5]} | {boardData[2][6]} {boardData[2][7]} {boardData[2][8]} |
        -------------------------
        | {boardData[3][0]} {boardData[3][1]} {boardData[3][2]} | {boardData[3][3]} {boardData[3][4]} {boardData[3][5]} | {boardData[3][6]} {boardData[3][7]} {boardData[3][8]} |
        | {boardData[4][0]} {boardData[4][1]} {boardData[4][2]} | {boardData[4][3]} {boardData[4][4]} {boardData[4][5]} | {boardData[4][6]} {boardData[4][7]} {boardData[4][8]} |
        | {boardData[5][0]} {boardData[5][1]} {boardData[5][2]} | {boardData[5][3]} {boardData[5][4]} {boardData[5][5]} | {boardData[5][6]} {boardData[5][7]} {boardData[5][8]} |
        -------------------------
        | {boardData[6][0]} {boardData[6][1]} {boardData[6][2]} | {boardData[6][3]} {boardData[6][4]} {boardData[6][5]} | {boardData[6][6]} {boardData[6][7]} {boardData[6][8]} |
        | {boardData[7][0]} {boardData[7][1]} {boardData[7][2]} | {boardData[7][3]} {boardData[7][4]} {boardData[7][5]} | {boardData[7][6]} {boardData[7][7]} {boardData[7][8]} |
        | {boardData[8][0]} {boardData[8][1]} {boardData[8][2]} | {boardData[8][3]} {boardData[8][4]} {boardData[8][5]} | {boardData[8][6]} {boardData[8][7]} {boardData[8][8]} |
        -------------------------
        """
    return b

def clean_terminal(row,col): # used to clean the terminal
    os.system('cls')
    if boardData[row][col] == "X":
        boardData[row][col] = "."

def move_right(): # moves the cursor to the right
    clean_terminal(pos[0],pos[1])
    if pos[1] < 8:
        pos[1] += 1
    elif pos[1] == 8 and pos[0] < 8:
        pos[1] = 0
        pos[0] += 1
    boardData[pos[0]][pos[1]] = "X"
    print(message,create_board())

def move_left(): # moves the cursor to the left
    clean_terminal(pos[0],pos[1])
    if pos[1] > 0:
        pos[1] -= 1
    elif pos[1] == 0 and pos[0] > 0:
        pos[1] = 8
        pos[0] -= 1
    boardData[pos[0]][pos[1]] = "X"
    print(message,create_board())

def move_up(): # moves the cursor up
    clean_terminal(pos[0],pos[1])
    if pos[0] > 0:
        pos[0] -= 1
    boardData[pos[0]][pos[1]] = "X"
    print(message,create_board())

def move_down(): # moves the cursor down
    clean_terminal(pos[0],pos[1])
    if pos[0] < 8:
        pos[0] += 1
    boardData[pos[0]][pos[1]] = "X"
    print(message,create_board())

def check_if_valid(row, col, num): # logic to check if the number is valid
    for i in range(9): #checking the row
        if boardData[row][i] == num:
            return False
    for i in range(9): #checking the column
        if boardData[i][col] == num:
            return False
    startRow = row - row % 3 #used to check the cells
    startCol = col - col % 3
    for i in range(3): #checking the cells
        for j in range(3):
            if boardData[i + startRow][j + startCol] == num:
                return False
    return True 
 
def solve_puzzle(row, col):
    startTime = datetime.now()
    if (row == 8 and col == 9):# if the solving function gets to this point, the board is solved and function is aborted, rerturns True
        return True
    if col == 9: # goes to the next row
        row += 1
        col = 0
    if boardData[row][col] != "." or boardData[row][col] == "X": # skips the cell if it is already filled
        return solve_puzzle(row, col + 1)
    for num in range(1, 10): # tries numbers 1-9
        if check_if_valid(row, col, num): # checks if the number is valid
            boardData[row][col] = num
            if solve_puzzle(row, col + 1): # recursively calls the function
                return True
        boardData[row][col] = "." # if the number is not valid, it is reset
        deltaTime = datetime.now() - startTime
        if deltaTime.total_seconds() > 5: # if the function takes longer than 5 seconds, it is aborted
            break
    return False 

def check_solution():
    logic = True
    for i in range(9): 
       if "." in boardData[i]:
            logic = False
    return logic

#main loop
boardData[pos[0]][pos[0]] = "X" # sets the starting position
print(message,create_board())
def on_key_release(key): # listens for key presses
    global solved
    if key == Key.right: 
        if solved == False:
            move_right()
    elif key == Key.left:
        if solved == False:
            move_left()
    elif key == Key.up:
        if solved == False:
            move_up()
    elif key == Key.down:
        if solved == False:
            move_down()
    elif key == Key.esc:
        print("Exiting...")
        sleep(1)
        exit()
    elif key == Key.enter:
        print("Solving...")
        for i in range(9): # removes the cursor from the board
            for j in range(9):
                if boardData[i][j] == "X":
                    boardData[i][j] = "."
        solved = True
        solve_puzzle(0,0)
        os.system('cls')
        if check_solution() == True:
            print("Solved!",create_board())
        else:
            print("No solution found.",create_board())
    else: # checks if the input is a number and if it is, it is entered into the board
        try: # using try except to catch invalid inputs (if key is pressed that is not number/letter it would crash the program otherwise)
            num = int(key.char)
            if num > 0:
                boardData[pos[0]][pos[1]] = num
                move_right()
        except:
            print("Invalid input.")
    
try: # used to catch errors
    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()
except:
    print("An error occured.")
    sleep(5)
    exit()