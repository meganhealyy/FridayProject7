# Define a dictionary with questions as keys and answers as values
trivia_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the largest planet in our solar system?": "Jupiter",
    "In what year did the Titanic sink?": "1912",
    "What is the chemical symbol for water?": "H2O"
}

# Greeting message
print("Welcome to the Trivia Quiz Game!")
print("Answer the following questions to test your knowledge.\n")

# For loop to go through each question in the dictionary
for question, correct_answer in trivia_questions.items():
    # Ask the user the question
    user_answer = input(question + " ")

    # Check if the user's answer matches the correct answer (case insensitive)
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!\n")
    else:
        print(f"Incorrect! The correct answer is: {correct_answer}\n")

# Farewell message
print("Thanks for playing! Hope you learned something new.")
