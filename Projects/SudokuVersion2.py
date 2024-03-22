# Sudoku solver by Jordin Myers
# solving steps are based on this wikipedia article https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#/media/File:Sudoku_solved_by_bactracking.gif

from time import sleep as sleep
from pynput import keyboard # pip install pynput
from pynput.keyboard import Key
import os

#set up board
r = { # creates a 9x9 board with all values set to "." - backend use
    i: ["."]*9 for i in range(9)
}
n = ['1','2','3','4','5','6','7','8','9'] # used to check if the input is a number
pos = [0,0] # starting position
s = False # used to check if the board is solved
message = """ 
Use the arrow keys to move the cursor and the number keys to enter a number.
Press esc to exit.
Press enter to submit.
""" # instructions

#functions
def board(): # creates the board that will be displayed to user
    b = f"""
        -------------------------
        | {r[0][0]} {r[0][1]} {r[0][2]} | {r[0][3]} {r[0][4]} {r[0][5]} | {r[0][6]} {r[0][7]} {r[0][8]} |
        | {r[1][0]} {r[1][1]} {r[1][2]} | {r[1][3]} {r[1][4]} {r[1][5]} | {r[1][6]} {r[1][7]} {r[1][8]} |
        | {r[2][0]} {r[2][1]} {r[2][2]} | {r[2][3]} {r[2][4]} {r[2][5]} | {r[2][6]} {r[2][7]} {r[2][8]} |
        -------------------------
        | {r[3][0]} {r[3][1]} {r[3][2]} | {r[3][3]} {r[3][4]} {r[3][5]} | {r[3][6]} {r[3][7]} {r[3][8]} |
        | {r[4][0]} {r[4][1]} {r[4][2]} | {r[4][3]} {r[4][4]} {r[4][5]} | {r[4][6]} {r[4][7]} {r[4][8]} |
        | {r[5][0]} {r[5][1]} {r[5][2]} | {r[5][3]} {r[5][4]} {r[5][5]} | {r[5][6]} {r[5][7]} {r[5][8]} |
        -------------------------
        | {r[6][0]} {r[6][1]} {r[6][2]} | {r[6][3]} {r[6][4]} {r[6][5]} | {r[6][6]} {r[6][7]} {r[6][8]} |
        | {r[7][0]} {r[7][1]} {r[7][2]} | {r[7][3]} {r[7][4]} {r[7][5]} | {r[7][6]} {r[7][7]} {r[7][8]} |
        | {r[8][0]} {r[8][1]} {r[8][2]} | {r[8][3]} {r[8][4]} {r[8][5]} | {r[8][6]} {r[8][7]} {r[8][8]} |
        -------------------------
        """
    return b

def clean(row,col): # used to clean the terminal
    os.system('cls')
    if r[row][col] == "X":
        r[row][col] = "."

def right(): # moves the cursor to the right
    clean(pos[0],pos[1])
    if pos[1] < 8:
        pos[1] += 1
    elif pos[1] == 8 and pos[0] < 8:
        pos[1] = 0
        pos[0] += 1
    r[pos[0]][pos[1]] = "X"
    print(message,board())

def left(): # moves the cursor to the left
    clean(pos[0],pos[1])
    if pos[1] > 0:
        pos[1] -= 1
    elif pos[1] == 0 and pos[0] > 0:
        pos[1] = 8
        pos[0] -= 1
    r[pos[0]][pos[1]] = "X"
    print(message,board())

def up(): # moves the cursor up
    clean(pos[0],pos[1])
    if pos[0] > 0:
        pos[0] -= 1
    r[pos[0]][pos[1]] = "X"
    print(message,board())

def down(): # moves the cursor down
    clean(pos[0],pos[1])
    if pos[0] < 8:
        pos[0] += 1
    r[pos[0]][pos[1]] = "X"
    print(message,board())

def check(row, col, num): # logic to check if the number is valid
    for i in range(9): #checking the row
        if r[row][i] == num:
            return False
    for i in range(9): #checking the column
        if r[i][col] == num:
            return False
    startRow = row - row % 3 #used to check the cells
    startCol = col - col % 3
    for i in range(3): #checking the cells
        for j in range(3):
            if r[i + startRow][j + startCol] == num:
                return False
    return True 
 
def solve(row, col):
    if (row == 8 and col == 9):# if the solving function gets to this point, the board is solved and function is aborted, rerturns True
        return True
    if col == 9: # goes to the next row
        row += 1
        col = 0
    if r[row][col] != "." or r[row][col] == "X": # skips the cell if it is already filled
        return solve(row, col + 1)
    for num in range(1, 10): # tries numbers 1-9
        if check(row, col, num): # checks if the number is valid
            r[row][col] = num
            if solve(row, col + 1): # recursively calls the function
                return True
        r[row][col] = "." # if the number is not valid, it is reset
    return False 

def solution():
    logic = True
    for i in range(9): 
       if "." in r[i]:
            logic = False
    return logic

#main loop
r[pos[0]][pos[0]] = "X" # sets the starting position
print(message,board())
def on_key_release(key): # listens for key presses
    global s
    if key == Key.right: 
        if s == False:
            right()
    elif key == Key.left:
        if s == False:
            left()
    elif key == Key.up:
        if s == False:
            up()
    elif key == Key.down:
        if s == False:
            down()
    elif key == Key.esc:
        print("Exiting...")
        sleep(1)
        exit()
    elif key == Key.enter:
        print("Solving...")
        print(str(solve(0,0)))
        for i in range(9): # removes the cursor from the board
            for j in range(9):
                if r[i][j] == "X":
                    r[i][j] = "."
        solve(0,0)
        if solution() == True:
            s = True
            os.system('cls')
            print("Solved!",board())
        else:
            s = True
            os.system('cls')
            print("No solution found.",board())
    else: # checks if the input is a number and if it is, it is entered into the board
        try: # using try except to catch invalid inputs (if key is pressed that is not number/letter it would crash the program otherwise)
            if key.char in n:
                num = int(key.char)
                r[pos[0]][pos[1]] = num
                right()
        except:
            print("Invalid input.")
    
try: # used to catch errors
    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()
except:
    print("An error occured.")
    sleep(5)
    exit()