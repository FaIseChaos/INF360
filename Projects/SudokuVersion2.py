# Sudoku solver 
# 1. Read the input from the user
# 2. Check if the input is solvable
# 3. Solve the puzzle
# 4. Print the solution

from time import sleep as sleep
from pynput import keyboard # pip install pynput
from pynput.keyboard import Key
import os

#set up board data
r = {
    0: [".",".",".",".",".",".",".",".","."],
    1: [".",".",".",".",".",".",".",".","."],
    2: [".",".",".",".",".",".",".",".","."],
    3: [".",".",".",".",".",".",".",".","."],
    4: [".",".",".",".",".",".",".",".","."],
    5: [".",".",".",".",".",".",".",".","."],
    6: [".",".",".",".",".",".",".",".","."],
    7: [".",".",".",".",".",".",".",".","."],
    8: [".",".",".",".",".",".",".",".","."]
}

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
    r[row][col] = "."

def loc(row,col):
    r[row][col] = "X"

pos = [0,0]

#main loop
def on_key_release(key):
    if key == Key.right:
        clean(pos[0],pos[1])
        if pos[1] < 8:
            pos[1] += 1
        elif pos[1] == 8 and pos[0] < 8:
            pos[1] = 0
            pos[0] += 1
        loc(pos[0],pos[1])
        print(board())
    if key == Key.left:
        clean(pos[0],pos[1])
        if pos[1] > 0:
            pos[1] -= 1
        elif pos[1] == 0 and pos[0] > 0:
            pos[1] = 8
            pos[0] -= 1
        loc(pos[0],pos[1])
        print(board())
    if key == Key.up:
        clean(pos[0],pos[1])
        if pos[0] > 0:
            pos[0] -= 1
        loc(pos[0],pos[1])
        print(board())
    if key == Key.down:
        clean(pos[0],pos[1])
        if pos[0] < 8:
            pos[0] += 1
        loc(pos[0],pos[1])
        print(board())
    if key == Key.esc:
        exit()
    if key == Key.space:
        print(r)

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()

#sleep(3)
#clean