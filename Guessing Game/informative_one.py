# For this particular project, we need the program to be able
# to generate a random number between x and y. 
import random

# We need to generate a new random that ONLY THE PROGRAM KNOWS.
# This function below generates a number between
# 1 and 100 inclusively(meaning that 1 and 100 is also included).
rand = random.randint(1, 100)

# You can do this too ! This will output exactly the same value.
rand = int(random.random() * 100)

# Just for cool
print("Welcome to guessing game v1.0 !")

# Because we need the user to input the number endlessly,
# We have to put the main program in a always-running loop.

# Doing while(true) in python puts everything inside it in a
# NEVERENDING loop, until `break` is called.

# You can change "True" into a statement, just like an if statement.
while (True):

    # Yes, you can put function inside of functions.
    # The innermost function gets executed first, then right, and moving outward
    # until all functions is ran, then we go to the next line.

    # The code below means that the program prints whats inside of `input()`, then
    # waits for the user to input ANYTHING into the terminal, then press ENTER.

    # The program will insert it to a variable.
    # Note: the `input()` function will return a STRING(str).
    guess = input("Input a number: ")

    # The program then will check whether every character in the string
    # is a number. If not, then the program will print a warning, and
    # `continue` is called. 
    # `continue` means that the programmer wants to restart the loop.
    if ( not str(guess).isnumeric()):
        print("The text inputted is not a number !")
        continue
    
    # Then, python tries to convert it into an INTEGER(Bilangan Bulat)
    # and put into the guess variable.
    guess = int(guess)

    # The program then compares the converted user input with
    # THE GENERATED NUMBER by the program in line 8
    if (guess > rand):
        print("Number too high. Guess again!")
    elif (guess < rand):
        print("Number too low. Guess again!")

    # Both the conditions above just checks whether the number is more AND less
    # than the generated number. This means that the EQUALS has not been checked by if.
    # Therefore, the below statement automatically means that `if (guess == rand)`
    else:
        print("Congratulations ! You win nothing.")
        break