import random

rand = random.randint(1, 100)
print("Welcome to guessing game v1.0 !")

while (True):

    guess: str = input("Input a number: ")
    if (not guess.isnumeric()):
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if (guess > rand):
        print("Number too high. Guess again!")
    elif (guess < rand):
        print("Number too low. Guess again!")
    else:
        print("Congratulations ! You win nothing.")
        break