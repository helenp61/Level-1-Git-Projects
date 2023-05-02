"""Simple version of Rock, Paper, Scissors"""

# Import random module
import random

# Create a list of play options
play = ["Rock", "Paper", "Scissors"]

# Setup player (computer and you)
# Assign a random play to the system

computer = play[random.randint(0, 2)]  # method to assign random number
# between 0 and 2 which corresponds to each of the three play options

# Set player to False
player = False


# Craete game using while loop

while player == False:
    # Set the player to True
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)
    else:
        print("That's not a valid play. Check the spelling!")
    # Player was set to True, but we want it to be False so the loop continues
    player = False
    computer = play[random.randint(0, 2)]
