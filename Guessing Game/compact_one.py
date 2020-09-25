import random

rand = random.randint(1, 100)
print("Welcome to guessing game v1.0 !")

while (True):

    guess = int(input("Input a number: "))

    if (guess > rand):
        print("Number too high. Guess again!")
    elif (guess < rand):
        print("Number too low. Guess again!")
    else:
        print("Congratulations ! You win nothing.")
        break