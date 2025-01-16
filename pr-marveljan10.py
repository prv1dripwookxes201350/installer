os.system('cls')
import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to make your move.")
    print("Type 'quit' to exit the game.")

    # Choices
    options = ["rock", "paper", "scissors"]

    while True:
        # Get player's move
        player_move = input("\nYour move: ").lower()
        
        if player_move == "quit":
            print("Thanks for playing! Goodbye!")
            break
        elif player_move not in options:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Computer's move
        computer_move = random.choice(options)
        print(f"Computer chose: {computer_move}")

        # Determine the winner
        if player_move == computer_move:
            print("It's a tie!")
        elif (player_move == "rock" and computer_move == "scissors") or \
             (player_move == "paper" and computer_move == "rock") or \
             (player_move == "scissors" and computer_move == "paper"):
            print("You win!")
        else:
            print("You lose!")

rock_paper_scissors()
exit()

os.system('cls')
print("GAME OVER...")
input()
exit()
