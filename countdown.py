import random
import time

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def get_prediction():
    # Replace this with the code for your computer vision model
    # The model should return the predicted class based on the camera input
    # Assuming the model returns the predicted class name as 'prediction'
    prediction = "Rock"  # Example prediction
    return prediction

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

    print("Rock-Paper-Scissors!")
    countdown = 3
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)

    user_choice = get_prediction()

    print("You chose", user_choice)
    print("Computer chose", computer_choice)

    winner = get_winner(computer_choice, user_choice)
    print(winner)

# Call the play function to start the game
play()


#used abit of help