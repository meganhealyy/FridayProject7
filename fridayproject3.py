# Importing the random module to generate a random number
import random

# Greeting the user and asking if they want to play the game
print("Welcome to the Number Guessing Game!")
play_game = input("Do you want to play the game? (yes/no): ").lower()

# If the user chooses not to play
if play_game == 'no':
    print("Maybe next time!")
# If the user chooses to play
elif play_game == 'yes':
    # Generate a random secret number between 1 and 10
    secret_number = random.randint(1, 10)

    # Initialize the user's guess to None (to start the loop)
    user_guess = None

    # Keep asking the user to guess until they guess correctly
    while user_guess != secret_number:
        # Ask the user to guess a number between 1 and 10
        user_guess = int(input("Guess a number between 1 and 10: "))

        # Check if the guess is correct
        if user_guess == secret_number:
            print("Congratulations! You've guessed the number!")
        else:
            print("Try again!")

# If the user enters something other than 'yes' or 'no'
else:
    print("Please enter 'yes' or 'no'.")

# Farewell message
print("\nThanks for playing the Number Guessing Game. Goodbye!")
