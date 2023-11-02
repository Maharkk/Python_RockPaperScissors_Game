import random

# Function to determine the winner based on choices
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to get the computer's choice randomly
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to play the game
def play_game():
    print("Let's play Rock, Paper, Scissors!")
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    # Check if user input is valid
    if user_choice in ["rock", "paper", "scissors"]:
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
        print(determine_winner(user_choice, computer_choice))
    else:
        print("Invalid choice. Please enter rock, paper, or scissors.")

# Play the game
play_game()

# Random module helps to pick random choices 