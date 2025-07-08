import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
number = random.randint(1, 10)
tries = 3  

while tries > 0:
    print(f"\nYou have {tries} tries left.")
    guess = int(input("Guess the number: "))
    tries -= 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number correctly.")
        break
else:
    print(f"Sorry, you've run out of tries. The number was {number}.")
    print("Better luck next time.")
