# Notes on What Each Line of Code Does in Friday Project 1:

print("Welcome to the Mad Libs game!"):
This line prints a welcome message to the user, letting them know the game has started.

print("Please provide the following words to complete your story:"):
Prints instructions telling the user they will need to provide words to fill in the blanks for the story.

large_object = input("Enter a large object: "):
Prompts the user to enter a large object (singular). The input is stored in the variable large_object.

large_objects_plural = input("Enter large objects (plural): "):
Prompts the user to enter multiple large objects (plural). The input is stored in the variable large_objects_plural.

adjective = input("Enter an adjective: "):
Prompts the user to provide an adjective. The input is stored in the variable adjective.

body_part = input("Enter a body part: "):
Prompts the user to enter the name of a body part. The input is stored in the variable body_part.

restaurant = input("Enter the name of a restaurant: "):
Prompts the user to provide the name of a restaurant. The input is stored in the variable restaurant.

food_1 = input("Enter a type of food: "):
Prompts the user for a type of food (first food). The input is stored in food_1.

food_2 = input("Enter another type of food: "):
Prompts the user for a second type of food. The input is stored in food_2.

mad_lib_story = f""" ... """:
This section creates the actual story template using an f-string, where the placeholders {} are replaced by the user's inputs. It forms the final story and stores it in the mad_lib_story variable.

print("\nHere is your completed Mad Lib story:"):
Prints a message indicating that the Mad Lib story is about to be displayed.

print(mad_lib_story):
Outputs the completed Mad Lib story, using the user's inputs in place of the placeholders.

# Notes on What Each Line of Code Does in Friday Project 2:
import random:
Imports the random module, which contains the randint function used to generate random numbers.

print("Welcome to the PowerBall Lottery Number Generator!"):
Displays a greeting message to welcome the user and explain the program’s purpose.

print("This program will generate 6 random numbers for your PowerBall ticket."):
Further explains to the user that the program will generate random numbers for their PowerBall ticket.

white_ball_1 = random.randint(1, 69):
Generates the first random number between 1 and 69 (for the white ball) and stores it in the variable white_ball_1.

white_ball_2 = random.randint(1, 69):
Generates the second random number between 1 and 69 (for the white ball) and stores it in the variable white_ball_2.

white_ball_3 = random.randint(1, 69):
Generates the third random number between 1 and 69 (for the white ball) and stores it in the variable white_ball_3.

white_ball_4 = random.randint(1, 69):
Generates the fourth random number between 1 and 69 (for the white ball) and stores it in the variable white_ball_4.

white_ball_5 = random.randint(1, 69):
Generates the fifth random number between 1 and 69 (for the white ball) and stores it in the variable white_ball_5.

red_ball = random.randint(1, 26):
Generates a random number between 1 and 26 for the red ball and stores it in the variable red_ball.

print(f"\nYour PowerBall numbers are: {white_ball_1} {white_ball_2} {white_ball_3} {white_ball_4} {white_ball_5} {red_ball}"):
This prints the generated PowerBall numbers in the specified format, with one space between the first five white balls and three spaces between the last white ball and the red ball.

print("\nGood luck! Thank you for using the PowerBall Lottery Number Generator."):
Displays a farewell message to the user, wishing them good luck and thanking them for using the program.

# Notes On What Each Line of Code Does in Friday Project 3:
import random:
Imports the random module, which allows us to use randint to generate a random number.

print("Welcome to the Number Guessing Game!"):
Displays a greeting message, welcoming the user to the game.

play_game = input("Do you want to play the game? (yes/no): ").lower():
Asks the user if they want to play the game. The lower() method converts their input to lowercase to handle cases where the user types "Yes" or "YES", etc.

if play_game == 'no'::
Checks if the user enters "no" and proceeds with the condition to quit the game.

print("Maybe next time!"):
Displays a message telling the user that they can play another time if they chose not to play.

elif play_game == 'yes'::
Checks if the user enters "yes" and proceeds with starting the game.

secret_number = random.randint(1, 10):
Generates a random secret number between 1 and 10 that the user will try to guess. It’s stored in the variable secret_number.

user_guess = None:
Initializes user_guess to None to ensure the loop starts. This will store the user’s guesses.

while user_guess != secret_number::
Starts a loop that continues until the user guesses the correct number.

user_guess = int(input("Guess a number between 1 and 10: ")):
Prompts the user to enter a number between 1 and 10, converting their input to an integer.

if user_guess == secret_number::
Checks if the user's guess matches the randomly generated secret number.

print("Congratulations! You've guessed the number!"):
If the guess is correct, this message congratulates the user.

else::
If the guess is incorrect, the program will proceed to the next block of code.

print("Try again!"):
Informs the user that their guess was wrong and asks them to try again.

else: (outside the if-elif block):
Catches any input that isn’t "yes" or "no", asking the user to enter valid options.

print("\nThanks for playing the Number Guessing Game. Goodbye!"):
Displays a farewell message, thanking the user for playing after they either guessed correctly or chose not to play.

# Notes On What Each Line Does in Friday Project 4
trivia_questions = { ... }:
Defines a dictionary where the keys are trivia questions and the values are their corresponding correct answers.

print("Welcome to the Trivia Quiz Game!"):
Displays a welcome message to the user, explaining the purpose of the program.

for question, correct_answer in trivia_questions.items()::
A for loop that iterates through the dictionary. question holds the question (key) and correct_answer holds the correct answer (value).

user_answer = input(question + " "):
Displays each question to the user and captures their response using the input() function.

if user_answer.strip().lower() == correct_answer.lower()::
Checks if the user's answer (after stripping any extra spaces and converting it to lowercase) matches the correct answer (also converted to lowercase). This makes the comparison case-insensitive.

print("Correct!\n"):
If the user's answer matches the correct answer, it prints "Correct!" and moves to the next question.

print(f"Incorrect! The correct answer is: {correct_answer}\n"):
If the user's answer is incorrect, it displays the correct answer to the user.

print("Thanks for playing! Hope you learned something new."):
Displays a farewell message to the user after all questions have been asked. 

# Notes on What Each Line of Code Does in Friday Project 5:
def redText(text)::
Defines a function that takes text as input and formats it in red using ANSI escape codes. \033[31m sets the color to red, and \033[0m resets it to the default color.

def blueText(text)::
Defines a function that formats text in blue. The ANSI escape code \033[34m is used to set the color to blue.

def greenText(text)::
Defines a function that formats text in green using the ANSI code \033[32m.

def yellowText(text)::
Defines a function that formats text in yellow using \033[33m.

def brownText(text)::
Defines a function that formats text in brown using an extended ANSI code \033[38;5;94m (brown is often represented as dark yellow in terminal color schemes).

def main()::
Main program logic to demonstrate the color functions and handle user input.

print(redText("This is red text!")):
Calls the redText() function and prints the text in red. Similarly, the other print() statements demonstrate other colors.

color_choice = input("Enter your color choice: ").lower():
Asks the user to input a color choice. The .lower() method ensures the input is in lowercase for easier comparison.

user_text = input("Enter the text you want to display in that color: "):
Asks the user for the text they want to display.

if color_choice == "red"::
Checks the user's color choice and calls the corresponding function to display the text in that color.

else::
If the user enters an invalid color, the program prints an error message.

# Notes On What Each Line Does in Friday Project 6:
class BankAccount::
Defines a class called BankAccount to encapsulate bank account functionality.

def __init__(self, account_number)::
Initializes a new instance of the BankAccount class, taking an account number as a parameter.

self.account_number = account_number:
Assigns the provided account number to the instance variable account_number.

self.balance = 0:
Initializes the balance attribute to 0 when a new bank account is created.

def deposit(self, amount)::
Defines a method to deposit money into the account.

if amount > 0::
Checks if the deposit amount is positive.

self.balance += amount:
Increases the balance by the deposited amount.

print(f"Deposited ${amount}. New balance is ${self.balance}."):
Prints a confirmation message showing the deposited amount and the new balance.

else::
Handles the case where the deposit amount is not positive.

print("Deposit amount must be positive!"):
Informs the user that the deposit amount must be positive.

def withdraw(self, amount)::
Defines a method to withdraw money from the account.

if 0 < amount <= self.balance::
Checks if the withdrawal amount is valid (positive and not greater than the balance).

self.balance -= amount:
Decreases the balance by the withdrawn amount.

print(f"Withdrew ${amount}. New balance is ${self.balance}."):
Prints a confirmation message showing the withdrawn amount and the new balance.

else::
Handles the case where the withdrawal amount is invalid.

print("Insufficient funds or invalid withdrawal amount!"):
Informs the user that the withdrawal is not possible due to insufficient funds or invalid amount.

def check_balance(self)::
Defines a method to return the current balance of the account.

return self.balance:
Returns the current balance.

account = BankAccount("123456789"):
Creates an instance of the BankAccount class with a sample account number.

while True::
Starts an indefinite loop for user interaction.

account_number_input = input("Please enter your account number (or 'exit' to quit): "):
Prompts the user to enter their account number or exit.

if account_number_input.lower() == "exit"::
Checks if the user wants to exit the program.

print("Thank you for using the banking system. Goodbye!"):
Displays a farewell message when the user decides to exit.

if account_number_input == account.account_number::
Verifies if the entered account number matches the account's number.

print("Options:"):
Displays available options for the user to choose from.

option = input("Choose an option (a/b/c): ").lower():
Prompts the user to select an option and converts the input to lowercase for easier comparison.

if option == 'a'::
Checks if the user chose to deposit money.

amount = float(input("Enter the amount to deposit: ")):
Prompts the user to enter the deposit amount and converts it to a float.

account.deposit(amount):
Calls the deposit method on the account instance to deposit the specified amount.

elif option == 'b'::
Checks if the user chose to withdraw money.

amount = float(input("Enter the amount to withdraw: ")):
Prompts the user to enter the withdrawal amount and converts it to a float.

account.withdraw(amount):
Calls the withdraw method on the account instance to withdraw the specified amount.

elif option == 'c'::
Checks if the user chose to check their balance.

balance = account.check_balance():
Calls the check balance method on the account instance and stores the balance.

print(f"Your current balance is: ${balance}."):
Displays the user's current balance.

else::
Handles the case where the user entered an invalid option.

print("Invalid option. Please try again."):
Informs the user that their choice was invalid.

else: (for account number check):
Handles the case where the account number entered does not match.

print("Account number does not match. Please try again."):
Informs the user that the account number entered is incorrect.
