import random

def declare_result(player, computer):
    if player == computer:
        return "It's a tie!"

    # Winning conditions
    if (player == 'rock' and computer == 'scissor') or \
       (player == 'scissor' and computer == 'paper') or \
       (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    option = ['rock', 'paper', 'scissor']
    
    while True:
        # User input
        print("\nRock, Paper, Scissor - Game Start!")
        player_choice = input("Enter your choice (rock, paper, scissor): ").lower()

        if player_choice not in option:
            print("Invalid choice! Please try again.")
            continue

        # Computer randomly chooses
        computer_choice = random.choice(option)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result =declare_result(player_choice, computer_choice)
        print(f"Result: {result}")

        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
