from rich.console import Console
from cli_maker.ui import Prompt
import time
import random

# Console
console = Console()

# Options and stuff
print()
console.print("R = Rock", style="bold blue")
console.print("P = Paper", style="bold blue")
console.print("S = Scissors", style="bold blue")


# Prompt
prompt = Prompt("green")

# Ask for choice
for i in range(0,5):
    time.sleep(.5)
    console.print("\n-----------Start----------", style="bold magenta")

    print()

    player = prompt.input("Player : ")
    computer = random.choice(["R", "P", "S"])

    draw = False
    winner = None

    if player == "R" and computer == "P":
        winner = "Computer"

    elif player == "P" and computer == "R":
        winner = "Player"

    elif player == "P" and computer == "S":
        winner = "Computer"

    elif player == "S" and computer == "P":
        winner = "Player"

    elif player == "S" and computer == "R":
        winner = "Computer"

    elif player == "R" and computer == "S":
        winner = "Player"

    elif player == computer:
        draw = True


    print()

    time.sleep(.5)
    console.print(f"Player : {player}", style="bold green")
    console.print(f"Computer : {computer}", style="bold red")
    time.sleep(.5)

    if winner != None:
        
        if winner == "Computer":
            console.print(f"\nWinner : {winner}", style="bold red")
        elif winner == "Player":
            console.print(f"\nWinner : {winner}", style="bold green")

    if draw:
        console.print(f"\nDraw", style="bold blue")


console.print("\n\n--------Thank You--------\n\n", style="bold green")