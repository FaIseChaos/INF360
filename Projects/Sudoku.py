# Sudoku solver 
# 1. Read the input from the user
# 2. Check if the input is solvable
# 3. Solve the puzzle
# 4. Print the solution

import turtle

# Set up the screen
screen = turtle.getscreen()
screen.title("Sudoku Solver by Jordin Myers")
screen.bgcolor("white")
screen.setup(width=900, height=900)
#screen.tracer(0)

# set up sudoku grid
maxX = 300 
maxY = 300

t = turtle.Turtle()
t.speed(0)

t.pensize(3)
t.penup()
t.goto(-1*maxX,maxY)
t.pendown()
t.goto(maxX,maxY)
t.goto(maxX,-1*maxY)
t.goto(-1*maxX,-1*maxY)
t.goto(-1*maxX,maxY)
t.goto(maxX/3,maxY)
t.goto(maxX/3,-1*maxY)
t.goto(-1*maxX/3,-1*maxY)
t.goto(-1*maxX/3,maxY)
t.penup()
t.goto(-1*maxX,maxY/3)
t.pendown()
t.goto(maxX,maxY/3)
t.goto(maxX,-1*maxY/3)
t.goto(-1*maxX,-1*maxY/3)

t.pensize(1)
t.penup()
t.goto(-1*maxX/9,maxY)
t.pendown()
t.goto(-1*maxX/9,-1*maxY)
t.goto(maxX/9,-1*maxY)
t.goto(maxX/9,maxY)
t.goto(2*maxX/9,maxY)
t.goto(2*maxX/9,-1*maxY)
t.goto(3*maxX/9,-1*maxY)
t.goto(3*maxX/9,maxY)


input("Press enter to exit...")
if input == " ":
    t.done()
