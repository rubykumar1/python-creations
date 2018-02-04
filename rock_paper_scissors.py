# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:13:07 2017

@author: Ruby Kumar

EXERCISE: Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
"""
import random

def game():
    options = ["rock", "paper", "scissors"]
    user_move = input("Enter 'rock', 'paper', or 'scissors'. Type 'quit' to exit: ")
    
    if user_move != "quit":
        #print("here")
        if user_move != "rock" and user_move != "paper" and user_move != "scissors":
            print("Oops! That's not valid.")
            #break
        else: 
            #continue
            comp_move = random.choice(options)
            print(comp_move)
            print("Computer's move: " + comp_move)
            if comp_move == "rock" and user_move == "scissors":
                print("Computer wins!")
            elif comp_move == "scissors" and user_move == "paper":
                print("Computer wins!")
            elif comp_move == "paper" and user_move == "rock":
                print("Computer wins!")
            elif comp_move == "scissors" and user_move == "rock":
                print("User wins!")
            elif comp_move == "paper" and user_move == "scissors":
                print("User wins!")
            elif comp_move == "rock" and user_move == "paper":
                print("User wins!") 
            elif comp_move == "rock" and user_move == "rock":
                print("Tie!")
            elif comp_move == "paper" and user_move == "paper":
                print("Tie!")
            elif comp_move == "scissors" and user_move == "scissors":
                print("Tie!")
            #else: 
                #break
game()  
      
while True:
    again = input("Do you want to play again? Type 'yes' or 'no'. ")
    if (again != "yes") and (again != "no"):
        print("invalid response")
    elif again == "no":
        break;
    else:
        game()