import random

# Define questions and answers
questions = [
    ("What is the capital of France?", ["London", "Paris", "Rome", "Berlin"]),
    ("What is the largest continent?", ["Asia", "Africa", "North America", "South America"]),
    ("What is the most abundant element in the universe?", ["Hydrogen", "Helium", "Carbon", "Oxygen"]),
]

# Generate the quiz
for i, (question, options) in enumerate(questions):
    # Print the question
    print(f"{i+1}. {question}")

    # Shuffle the options
    random.shuffle(options)

    # Print the options
    for j, option in enumerate(options):
        print(f"  {j+1}) {option}")

    # Get the user's answer
    answer = int(input("Enter your answer (1-4): "))

    # Check if the answer is correct
    if answer == options.index(question.split()[2]):
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {options.index(question.split()[2]) + 1)}.")
