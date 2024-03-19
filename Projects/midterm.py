import sys

userInput = input()

try: int(userInput)
except ValueError:
     print("Error: Not a valid number")
     sys.exit

if userInput > 0 and userInput < 5:
     print ("This is a valid input")
else:
     print ("This is not a valid input")