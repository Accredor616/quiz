import json
import sys
import os

def load_questions(filename: str):
    """
    Load quiz questions from a JSON file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error loading questions: {e}")
        sys.exit(1)

def run_quiz(questions: list):
    """
    Run the quiz, clear console between interactions, validate input, tally score, and summarize answers.
    """
    score = 0
    total = len(questions)
    user_answers = []

    for idx, q in enumerate(questions, start=1):
        valid_keys = sorted(q['options'].keys())
        # Input loop: clear, show question, validate
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Question {idx}: {q['question']}")
            for key in valid_keys:
                print(f"  {key}) {q['options'][key]}")

            ans = input("Your answer (a/b/c/d): ").strip().lower()
            if ans in valid_keys:
                break
            print("Invalid choice. Please enter a, b, c, or d.")
            input("Press Enter to retry...")

        user_answers.append(ans)
        correct_key = q['answer'].lower()
        selected_text = q['options'][ans]
        correct_text = q['options'][correct_key]

        if ans == correct_key:
            print(f"Correct! You answered '{ans}) {selected_text}'.\n")
            score += 1
        else:
            print(
                f"Wrong. You answered '{ans}) {selected_text}'. "
                f"The correct answer was '{correct_key}) {correct_text}'.\n"
            )

        input("Press Enter to continue...")

    # Final summary
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"You scored {score} out of {total}.\n")
    print("Summary of your answers:")
    for idx, q in enumerate(questions, start=1):
        your = user_answers[idx - 1]
        your_text = q['options'][your]
        correct_key = q['answer'].lower()
        correct_text = q['options'][correct_key]
        print(f"{idx}. {q['question']}")
        print(f"   Your answer: {your}) {your_text}")
        print(f"   Correct answer: {correct_key}) {correct_text}\n")

if __name__ == '__main__':
    questions = load_questions('questions.json')
    run_quiz(questions)