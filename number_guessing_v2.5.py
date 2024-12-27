# Modules
import art
from random import randint

# Constants for game difficulty to avoid global variables
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Display hint about the game modes
print("Hint: easy mode has 10 attempts and hard mode has 5 attempts only.")


def game_difficulty(difficulty):
    while difficulty not in ["easy", "hard"]:
        print("Invalid input. Please enter a valid difficulty level.")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return EASY_ATTEMPTS if difficulty == "easy" else HARD_ATTEMPTS


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


# Restart the Game if the user wants to play again!
def game_restart():
    # Restart the Game if the user wants to play again!
    game_restart = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if game_restart == "yes":
        print("Let's play again!")
        start_game()
    else:
        print("Goodbye!")


# Main game loop
def game_start(attempts, random_number):
    # global attempts
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        user_guess_validation = user_guess(guess)
        if user_guess_validation == random_number:
            print(
                f"You got it! The answer was {random_number}, you win and you have {attempts} attempts left"
            )
            game_restart()
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
            game_restart()

# Main game function
def start_game():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = game_difficulty(difficulty)  # Set the number of attempts
    random_number = randint(1, 100)  # returns a number between 3 and 9 (both included)
    print(random_number)  # For testing purposes, remove this in the final game
    game_start(attempts, random_number)


# Start the game for the first time
start_game()
