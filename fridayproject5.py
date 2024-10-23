# Function to change text color to red
def redText(text):
    return f"\033[31m{text}\033[0m"  # 31 is the ANSI code for red

# Function to change text color to blue
def blueText(text):
    return f"\033[34m{text}\033[0m"  # 34 is the ANSI code for blue

# Function to change text color to green
def greenText(text):
    return f"\033[32m{text}\033[0m"  # 32 is the ANSI code for green

# Function to change text color to yellow
def yellowText(text):
    return f"\033[33m{text}\033[0m"  # 33 is the ANSI code for yellow

# Function to change text color to brown (brown is often rendered as dark yellow)
def brownText(text):
    return f"\033[38;5;94m{text}\033[0m"  # Using 38;5;94 for brown color (ANSI extended)

# Main program logic
def main():
    print("Welcome to the Colorful Text Display Program!")
    
    # Display each color for demonstration
    print(redText("This is red text!"))
    print(blueText("This is blue text!"))
    print(greenText("This is green text!"))
    print(yellowText("This is yellow text!"))
    print(brownText("This is brown text!"))
    
    # User input to select color and text
    print("\nChoose a color from the following options: red, blue, green, yellow, brown.")
    color_choice = input("Enter your color choice: ").lower()
    user_text = input("Enter the text you want to display in that color: ")

    # Call the corresponding function based on user choice
    if color_choice == "red":
        print(redText(user_text))
    elif color_choice == "blue":
        print(blueText(user_text))
    elif color_choice == "green":
        print(greenText(user_text))
    elif color_choice == "yellow":
        print(yellowText(user_text))
    elif color_choice == "brown":
        print(brownText(user_text))
    else:
        print("Invalid color choice!")

# Call the main function to run the program
main()
