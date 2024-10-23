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

