import random


def play_round(player_move, computer_move):
    # This function takes in the player's move and the computer's move and returns the outcome of the round.
    # Same as before

    moves = ["rock", "paper", "scissors"]


# Ask the user if they want to play a specific number of rounds or an infinite number of rounds.
num_rounds = None
while num_rounds is None:
    num_rounds_str = input(
        "How many rounds do you want to play? (Type 'inf' for infinite): ")
    if num_rounds_str == 'inf':
        num_rounds = float('inf')
    else:
        try:
            num_rounds = int(num_rounds_str)
        except ValueError:
            print("Invalid input. Please enter a positive integer or 'inf'.")

round_num = 1
player_score = 0
computer_score = 0

# Main game loop
while round_num <= num_rounds:
    print(f"Round {round_num}:")
    player_move = input("Rock, paper, or scissors? ")
    player_move = player_move.lower()

    # Check if the player wants to exit the game
    if player_move == "exit":
        break
    elif player_move not in moves:
        # If the player's move is not valid, print an error message and continue to the next round.
        print("Invalid move. Please try again.")
        continue

    # Generate a random move for the computer
    computer_move = random.choice(moves)
    print("Player: " + player_move)
    print("Computer: " + computer_move)

    # Determine the outcome of the round
    outcome = play_round(player_move, computer_move)
    print(outcome)

    # Update the scores based on the outcome of the round
    if outcome == "player wins":
        player_score += 1
    elif outcome == "computer wins":
        computer_score += 1

    round_num += 1

# Print the final score and determine the winner
if round_num > num_rounds:
    print("End of game. Final score:")
else:
    print("Game exited. Final score:")
print(f"Player: {player_score}")
print(f"Computer: {computer_score}")
if player_score > computer_score:
    print("Player wins!")
elif computer_score > player_score:
    print("Computer wins!")
else:
    print("Tie game.")
