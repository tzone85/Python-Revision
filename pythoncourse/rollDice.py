import random

roll = random.randint(1,6)
# print("The computer rolled: " + str(roll))

guess = int(input("Guess the dice roll:\n "))

if guess == roll:
    print("You guessed correctly! They rolled a " + str(roll))
else:
    print("You guessed wrong! They rolled a " + str(roll))