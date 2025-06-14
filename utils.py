import random

def get_user_input(num_options):
    while True:
        try:
            choice = int(input("Your answer (1-{}): ".format(num_options)))
            if 1 <= choice <= num_options:
                return choice
            else:
                print("Please enter a number between 1 and", num_options)
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_question():
    pass  


def get_question_by_difficulty(questions, difficulty):
    return random.choice([q for q in questions if q["difficulty"] == difficulty])

def update_difficulty(is_correct, current_difficulty):
    levels = ["easy", "medium", "hard"]
    index = levels.index(current_difficulty)

    if is_correct and index < 2:
        return levels[index + 1]  
    elif not is_correct and index > 0:
        return levels[index - 1]  
    else:
        return current_difficulty 
