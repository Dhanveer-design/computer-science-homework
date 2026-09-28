import random

secretNumber = random.randint(1, 100)

guess = 0
attempts = 0

print("Welcome to the Guess the Number Game!")
print("I am thinking of a number between 1 and 100.")

while guess != secretNumber:

    guess = int(input("Enter your guess: "))

    attempts = attempts + 1

    if guess < secretNumber:
        print("Too low! Try again.")

    elif guess > secretNumber:
        print("Too high! Try again.")

    else:
        print("Correct!")
        print("You guessed the number in", attempts, "attempts.")
