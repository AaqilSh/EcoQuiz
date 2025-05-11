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
