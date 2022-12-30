# Guess-the-number game
from random import *

number = randint(1, 20)
number_guessed = False

while number_guessed == False:
    userInput = int(input("Enter a number in the range of 1 to 20: "))

    if userInput == number:
        print("Perfect guess! The number is " + str(number))
        number_guessed = True

    # abs(number) -> returns absolute value
    # example abs(-2) = 2
    elif abs(userInput - number) < 3:   
        print("You are close, try again")

    else:
        print("Oops! Try again")