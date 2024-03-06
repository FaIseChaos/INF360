# INF360 - Programming in Python
# Jordin Myers
# Assignment 2

# [x] (1 point) - Initial comments*
# [x] (1 points) - Use at least 2 different comparison operators.
# [x] (1 points) - Use at least 1 boolean operator (and, or, not).
# [x] (2 points) - Write at least 1 if statement that MUST contain 2 elif statements and 1 else statement.
# [x] (2 points) - Write at least 1 while statement that contains a break and continue.
# [x] (2 points) - Write at least 1 for loop using the range() method.
# [x] (1 point) - Use the import keyword to import the random module. Use the random.randint() function somewhere in your script.

import time, fontstyle, sys, random #pip install fontstyle

intro = fontstyle.apply("Moony, Wormtail, Padfoot, and Prongs are proud to present the Marauder's Map!",'bold/underline')
print(intro)
nameQuestion = fontstyle.apply("What is your name?",'italic')
print(nameQuestion)
mapInput = input("> ")

def typeFunction(text):
    for char in text: #using 'text' instead of using 'range()' so it counts by the character instead of the position that the character is in
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0.01, 0.08)) #using 'random.uniform()' instead of 'random.randint()' so I can use float values instead of integers
    sys.stdout.write("\n")

def fiilchFunction():
    filchDistance = random.randint(1, 50)
    while filchDistance:
        print("Professor Filch is " + str(filchDistance) + " feet away.")
        filchDistance -= random.randint(-6, 6)
        time.sleep(.75)
        if filchDistance <= 5:
            print("Professor Filch is " + str(filchDistance) + " feet away.")
            print("Quick! Hide!")
            break
        continue

if mapInput == "Severus Snape":
    typeFunction(fontstyle.apply("Mr. Moony presents his compliments to Professor Snape and begs him to keep his abnormally large nose out of other people's business.",'italic/blue'))
    time.sleep(1)
    typeFunction(fontstyle.apply('Mr. Prongs agrees with Mr Moony, and would like to add that Professor Snape is an ugly git.','italic/red'))
    time.sleep(1)
    typeFunction(fontstyle.apply('Mr. Padfoot would like to register his astonishment that an idiot like that ever became a professor.','italic/green'))
    time.sleep(1)
    typeFunction(fontstyle.apply('Mr. Wormtail bids Professor Snape good day, and advises him to wash his hair, the slimeball.','italic/yellow'))
elif mapInput == "Moony" or mapInput == "Prongs" or mapInput == "Padfoot" or mapInput == "Wormtail":
    typeFunction(fontstyle.apply("Hello, old friend...",'italic'))
    mapInput = input("> ")
    if  mapInput == "I solemnly swear that I am up to no good." or mapInput =="bugtesting":
        fiilchFunction()
    elif mapInput == "mischief managed":
        typeFunction(fontstyle.apply("Goodbye, old friend...",'italic'))
    else:
        typeFunction("...")
else:
    typeFunction("Hello, " + mapInput + "...")
    mapInput = input("> ")
    if mapInput == "I solemnly swear that I am up to no good.":
        fiilchFunction()
    else:
        typeFunction("...")