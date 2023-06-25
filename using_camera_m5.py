import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def get_prediction():
    # Replace this with the code for your computer vision model
    # The model should return a list of probabilities for each class
    # Assuming the model returns a list named 'probabilities'
    probabilities = [0.8, 0.1, 0.05, 0.05]
    class_index = probabilities.index(max(probabilities))
    choices = ["Rock", "Paper", "Scissors", "Nothing"]
    return choices[class_index]

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It is a tie!"
    elif (
        (computer_choice == "Rock" and user_choice == "Scissors") or
        (computer_choice == "Paper" and user_choice == "Rock") or
        (computer_choice == "Scissors" and user_choice == "Paper")
    ):
        return "You lost"
    else:
        return "You won!"

def play():
    computer_choice = get_computer_choice()
    user_choice = get_prediction()

    print("Computer chose:", computer_choice)
    print("User chose:", user_choice)

    winner = get_winner(computer_choice, user_choice)
    print(winner)

# Call the play function to start the game
play()
