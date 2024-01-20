# INF360 - Programming in Python
# Jordin Myers
# Assignment 1

# (1 point) - Initial comments*
# (2 points) - Use of the print() function to display a welcome and prompt a question to the user.
# (2 points) - Use of the input() function and store in a variable called myInput.
# (1 point) - Use the print() function to print the contents of myInput.
# (2 points) - Use two different math operators from Table 1-1 in your script. This may be used to manipulate some input from the user.
# (2 points) - Use string concatenation

print("Welcome to my first Python program!")
print("What is your favorite color?")
myInput = input("> ")

print("Your favorite color is " + myInput + "?")
print("That's a great color!")
print("I like " + myInput + " too!")
print("What is your favorite integer?")
myInput = input("> ")

if myInput.isnumeric():
    print("Your favorite integer is " + myInput + "?")
    print("That's a great integer!")
    print(myInput + " times 2 is " + str(int(myInput) * 2) + "!")
    print(myInput + " plus 3 is " + str(int(myInput) + 3) + "!")
else:
    print("That's not an integer!")
    print("Please enter an integer next time!")