import json
from utils import ask_question, get_user_input

def load_questions(file_path="questions.json"):
    with open(file_path, "r") as f:
        return json.load(f)

def play_quiz():
    questions = load_questions()
    score = 0

    print("\n Welcome to the Eco Quiz Game!")
    print("Answer questions to test your environmental knowledge.\n")

    for i, q in enumerate(questions):
        print(f"Q{i+1}: {q['question']}")
        for idx, opt in enumerate(q['options'], 1):
            print(f"   {idx}. {opt}")

        choice = get_user_input(len(q['options']))
        chosen_answer = q['options'][choice - 1]

        if chosen_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")

    print(f"🎉 Quiz completed! Your score: {score}/{len(questions)}\n")

    again = input("Do you want to play again? (y/n): ").lower()
    if again == "y":
        play_quiz()

if __name__ == "__main__":
    play_quiz()
