import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    computer_choice = random.choice(choices)
    player_choice = input("Choose rock, paper, or scissors: ")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    rock_paper_scissors()
