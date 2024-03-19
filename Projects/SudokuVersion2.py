# Sudoku solver 
# 1. Read the input from the user
# 2. Check if the input is solvable
# 3. Solve the puzzle
# 4. Print the solution

import time
import os

#Set up board
print("""
-------------------------
| 5 3 . | . 7 . | . . . |
| 6 . . | 1 9 5 | . . . |
| . 9 8 | . . . | . 6 . |
-------------------------
| 8 . . | . 6 . | . . 3 |
| 4 . . | 8 . 3 | . . 1 |
| 7 . . | . 2 . | . . 6 |
-------------------------
| . 6 . | . . . | 2 8 . |
| . . . | 4 1 9 | . . 5 |
| . . . | . 8 . | . 7 9 |
-------------------------
""")

time.sleep(3)
clean = os.system('cls')
clean