# Lets play the game rock paper scissors

import random

options = ("Rock", "Paper", "Scissors")

is_running = True
score = 0
pc_score = 0

while is_running:

    pick = input("Please select - Rock, Paper or Scissors: ").capitalize()

    if pick not in options:
        print("Invalid choice, please choice again")
        continue

    # Computer picks (INSIDE the loop)
    computer = random.choice(options)
    print(f"Computer chose: {computer}")


## Setup the game scoring criteria

## Tie condition


    if pick == computer:
        print("Tie, Try again")
        continue

## Player wins conditions

    elif (pick == "Scissors" and computer == "Paper") or \
         (pick == "Rock" and computer == "Scissors" ) or \
         (pick == "Paper" and computer == "Rock"):
        
        score = score + 1


## Computer wins conditions

    else:

        pc_score = pc_score + 1    


## Display the score 


    print("----The Score----- ")
    print(f"Your Score - {score} Computer Score - {pc_score}")

    if score == 3 or pc_score == 3:
        print("Match Over")
        if score == 3:
            print("🎉 You won the match!")
        else:
            print("💀 Computer won the match!")
        is_running = False

