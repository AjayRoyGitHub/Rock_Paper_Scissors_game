# Rock ,Paper, Scissors Game

import random

user_wins = 0
computer_wins = 0
open_list = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter rock/paper/scissors or Q to quit from the game!!!: ").lower()
    if user_input == 'q':
        break
    if user_input not in open_list:
        continue

    random_number = random.randint(0, 2)      # rock : 0, paper : 1, scissors: 2
    computer_pick = open_list[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("Great, You Won !!!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("Great, You Won !!!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("Great, You Won !!!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Both inputs are same!! No Result!!")
    else:
        print("Sorry, You Lost!!!")
        computer_wins += 1

print("You won " + str(user_wins) + " times")
print("Computer won " + str(computer_wins) + " times")
print("Thank You for Playing this Game...Bye...")


