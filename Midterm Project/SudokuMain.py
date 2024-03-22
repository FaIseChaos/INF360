# Sudoku solver by Jordin Myers
# solving steps are based on this wikipedia article https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#/media/File:Sudoku_solved_by_bactracking.gif

from time import sleep as sleep
from pynput import keyboard # pip install pynput
from pynput.keyboard import Key
from SudokuFunctions import * # imports all the functions from the SudokuFunctions.py file

solved = False # used to check if the board is solved

#main loop
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
        solved = True
        enter_pressed()
    else: # checks if the input is a number and if it is, it is entered into the board
        try: # using try except to catch invalid inputs (if key is pressed that is not number/letter it would crash the program otherwise)
            num = int(key.char)
            input_number(num)
        except:
            print("Invalid input.")
    
try: # used to catch errors
    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()
except:
    print("An error occured.")
    sleep(5)
    exit()