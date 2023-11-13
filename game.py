import json
import random

def load_data(filepath):
    # Load the dataset from the given file path, assuming each line is a separate JSON object
    headlines_data = []
    with open(filepath, 'r') as file:
        for line in file:
            headlines_data.append(json.loads(line))
    return headlines_data

def play_game(headlines_data, number_of_questions):
    # Shuffle the data to get random headlines
    random.shuffle(headlines_data)

    # Initialize score and a list to keep track of incorrect guesses for summary
    score = 0
    incorrect_guesses = []

    # Start the game loop
    for i in range(number_of_questions):
        headline = headlines_data[i]
        print(f"\nHeadline {i+1}: {headline['headline']}")
        print("Is this headline from The Onion (type 'o') or the Huffington Post (type 'h')?")
        
        user_guess = ''
        while user_guess not in ['o', 'h']:
            user_guess = input("Your guess: ").lower()
            if user_guess not in ['o', 'h']:
                print("Invalid input. Please type 'o' for The Onion or 'h' for the Huffington Post.")
        
        # Check the answer and record incorrect guesses
        correct_answer = 'o' if headline['is_sarcastic'] == 1 else 'h'
        if user_guess != correct_answer:
            incorrect_guesses.append((i+1, headline['headline'], correct_answer))

        score += user_guess == correct_answer

    # Final score and summary
    incorrect_count = len(incorrect_guesses)
    success_rate = score / number_of_questions * 100
    print("\nGame Over! Here's your summary:")
    print(f"Number correct: {score}")
    print(f"Number incorrect: {incorrect_count}")
    print(f"Success rate: {success_rate:.2f}%")

    # If there are incorrect guesses, show them
    if incorrect_guesses:
        print("\nHere are the headlines you guessed incorrectly:")
        for index, headline, correct_answer in incorrect_guesses:
            print(f"{index}. {headline} (Correct answer: {'The Onion' if correct_answer == 'o' else 'The Huffington Post'})")

def main():
    # File path to the dataset
    filepath = 'Sarcasm_Headlines_Dataset_v2.json'  # Update with the correct path
    headlines_data = load_data(filepath)

    question_options = {
        '1': 20,
        '2': 50,
        '3': 100
    }

    number_of_questions = 0
    while number_of_questions == 0:
        number_of_questions_input = input("How many questions do you want to answer?\nType '1' for 20, '2' for 50, '3' for 100 questions: ")
        if number_of_questions_input in question_options:
            number_of_questions = question_options[number_of_questions_input]
        else:
            print("Invalid choice. Please type '1', '2', or '3'.")

    play_game(headlines_data, number_of_questions)

if __name__ == "__main__":
    main()
