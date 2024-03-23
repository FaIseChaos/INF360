from datetime import datetime
import os

#set up board
boardData = { # creates a 9x9 board with all values set to "." - backend use
    i: ["."]*9 for i in range(9)
}
pos = [0,0] # starting position
message = """ 
Use the arrow keys to move the cursor and the number keys to enter a number.
Press esc to exit.
Press enter to submit.
"""

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

def input_number(num): # puts a number on the board
    if num > 0:
        boardData[pos[0]][pos[1]] = num
        move_right()

def enter_pressed(): # removes the cursor from the board, solves puzzle, prints the solution if exists
    print("Solving...")
    for i in range(9): 
        for j in range(9):
            if boardData[i][j] == "X":
                boardData[i][j] = "."
    solve_puzzle(0,0)
    os.system('cls')
    if check_solution() == True:
        print("Solved!",create_board())
    else:
        print("No solution found.",create_board())

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
 
def solve_puzzle(row, col): # recursive function to solve the puzzle
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

def check_solution(): # checks if the board is solved
    logic = True
    for i in range(9): 
       if "." in boardData[i]:
            logic = False
    return logic

boardData[pos[0]][pos[1]] = "X" # sets the starting position
print(message,create_board()) # prints the board and instructions