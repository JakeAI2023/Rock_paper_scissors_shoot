#Rock paper scissors
import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_picked = options[random_number]
    print("Computer picked", computer_picked + ".")

    if user_input == "rock" and computer_picked == "scissors":
        print("You Won!!")
        user_score += 1
    elif user_input == "paper" and computer_picked == "rock":
        print("You Won!!")
        user_score += 1
    elif user_input == "scissors" and computer_picked == "paper":
        print("You Won!!")
        user_score += 1
    else:
        print("You lost!!")
        computer_score += 1
    
print("You won", user_score, "times.")
print("Computer won", computer_score, "times.")