import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Rock/Paper/Scissors): ").capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

# Example usage
computer_choice = get_computer_choice()
user_choice = get_user_choice()

print("Computer chose:", computer_choice)
print("User chose:", user_choice)


#figuring out who won 
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


computer_choice = get_computer_choice()
user_choice = get_user_choice()

print("Computer chose:", computer_choice)
print("User chose:", user_choice)

winner = get_winner(computer_choice, user_choice)
print(winner)
