import random
options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

is_running = True


while is_running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Player enter a choice from rock, paper or scissors : ").lower()
    print(f"Computer chose {computer}")
    print(f"Player chose {player}")
    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("YOU LOSE LMFAO!")
    if not input("Do you want to play again? (y/n) : ").lower() == "y":
        is_running = False
        break
print("Thank you for playing!")
