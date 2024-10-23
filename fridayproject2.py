# Importing the random module to use the randint function
import random

# Greeting the user and explaining the purpose of the program
print("Welcome to the PowerBall Lottery Number Generator!")
print("This program will generate 6 random numbers for your PowerBall ticket.")

# Generating the first 5 numbers (white balls) between 1 and 69
white_ball_1 = random.randint(1, 69)
white_ball_2 = random.randint(1, 69)
white_ball_3 = random.randint(1, 69)
white_ball_4 = random.randint(1, 69)
white_ball_5 = random.randint(1, 69)

# Generating the 6th number (red ball) between 1 and 26
red_ball = random.randint(1, 26)

# Printing the results in the requested format
print(f"\nYour PowerBall numbers are: {white_ball_1} {white_ball_2} {white_ball_3} {white_ball_4} {white_ball_5}   {red_ball}")

# Farewell message
print("\nGood luck! Thank you for using the PowerBall Lottery Number Generator.")
