# Modules
import art
import time
import random

# Variables
attempts = 0  # Initializing attempts variable

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Display hint about the game modes
print(
    "Hint: easy mode has 10 attempts and hard mode has 5 attempts only!", end="\r"
)  # Print the message on the same line
time.sleep(4)
print(" " * 50, end="\r")  # Overwrite the line with spaces


def game_difficulty(difficulty):
    while difficulty != "easy" and difficulty != "hard":
        print("Invalid input. Please enter a valid difficulty level.")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    return attempts


# Function to validate user's guess
def user_guess(guess):
    if not guess.isdigit():  # Check if input is a number
        print("Invalid input. Please enter a valid number.")
        return int(input("Make a guess: "))
    if int(guess) < 1 or int(guess) > 100:
        print("Please enter a number between 1 and 100.")
        return int(input("Make a guess: "))
    else:
        return int(guess)


# Get the game difficulty from the user
difficulty = input("So, lets choose a difficulty. Type 'easy' or 'hard': \n").lower()


# Set the number of attempts based on difficulty
attempts = game_difficulty(difficulty)

# Generate a random number between 1 and 100
random_number = random.randint(
    1, 100
)  # returns a number between 3 and 9 (both included)


# print(random_number)
# print(type(random_number))

# Main game loop
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    user_guess_validation = user_guess(guess)
    if user_guess_validation == random_number:
        print(
            f"You got it! The answer was {random_number} & left attempts are {attempts}."
        )
        break
    elif user_guess_validation < random_number:
        print("Too low.")
        attempts -= 1
    elif user_guess_validation > random_number:
        print("Too high.")
        attempts -= 1
    else:
        print(
            f"Your attempts are now {attempts}, So you've run out of guesses and you lose."
        )

# If no attempts are left, the user loses
if attempts == 0:
    print(
        f"You've run out of guesses, you lose. The correct answer was {random_number}"
    )
