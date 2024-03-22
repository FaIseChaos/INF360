# Sudoku solver 
# algorithm based on this wikipedia article https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#/media/File:Sudoku_solved_by_bactracking.gif
# 1. function that checks if row is valid
# 2. function that checks if column is valid
# 3. function that checks if box is valid

from time import sleep as sleep
from pynput import keyboard # pip install pynput
from pynput.keyboard import Key
import os
import fontstyle # pip install fontstyle

#set up board data
r = {
    i: ["."]*9 
    for i in range(9)
}

c = { # zip function, will do one "round" of the the "j" for loop first, then one "round" of the "i" for loop, then back to "j", then "i", etc.
    i: [r[j][i] for j in range(9)] 
    for i in range(9)
}

n = ['1','2','3','4','5','6','7','8','9']

pos = [0,0]

message = """
Use the arrow keys to move the cursor and the number keys to enter a number.
Press esc to exit.
Press enter to submit.
"""

#functions
def board():
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

def clean(row,col):
    os.system('cls')
    #r[row][col] = fontstyle.apply(str(r[pos[0]][pos[1]]),'WHITE/BLACK_BG')
    fontstyle.preserve(r[row][col])

def right():
    clean(pos[0],pos[1])
    if pos[1] < 8:
        pos[1] += 1
    elif pos[1] == 8 and pos[0] < 8:
        pos[1] = 0
        pos[0] += 1
    font = fontstyle.apply(str(r[pos[0]][pos[1]]),'BLACK/WHITE_BG')
    r[pos[0]][pos[1]] = font
    print(message,board())

def left():
    clean(pos[0],pos[1])
    if pos[1] > 0:
        pos[1] -= 1
    elif pos[1] == 0 and pos[0] > 0:
        pos[1] = 8
        pos[0] -= 1
    r[pos[0]][pos[1]] = fontstyle.apply(str(r[pos[0]][pos[1]]),'BLACK/WHITE_BG')
    print(message,board())

def up():
    clean(pos[0],pos[1])
    if pos[0] > 0:
        pos[0] -= 1
    r[pos[0]][pos[1]] = fontstyle.apply(str(r[pos[0]][pos[1]]),'BLACK/WHITE_BG')
    print(message,board())

def down():
    clean(pos[0],pos[1])
    if pos[0] < 8:
        pos[0] += 1
    r[pos[0]][pos[1]] = fontstyle.apply(str(r[pos[0]][pos[1]]),'BLACK/WHITE_BG')
    print(message,board())

def check(row, col, num):
    for i in range(9):
        if r[row][i] == num:
            return False
    for i in range(9):
        if r[i][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if r[i + startRow][j + startCol] == num:
                return False
    return True
 
def solve(row, col):
    if (row == 8 and col == 9):
        return True
    if col == 9:
        row += 1
        col = 0
    if r[row][col] != ".":
        return solve(row, col + 1)
    for num in range(1, 10): 
        if check(row, col, num):
            r[row][col] = num
            if solve(row, col + 1):
                return True
        r[row][col] = "."
    return False

#main loop
print(message,board())
def on_key_release(key):
    if key == Key.right:
        right()
    elif key == Key.left:
        left()
    elif key == Key.up:
        up()
    elif key == Key.down:
        down()
    elif key == Key.esc:
        print("Exiting...")
        sleep(1)
        exit()
    elif key == Key.space:
        print(r)
    elif key == Key.enter:
        print("Solving...")
        solve(0,0)
        os.system('cls')
        print(board())
    elif key.char in n:
        num = int(key.char)
        r[pos[0]][pos[1]] = num
        right()
        #return
    else:
        print("Invalid input1")
        return
    
with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()