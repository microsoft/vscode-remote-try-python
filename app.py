#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

rock = 1
paper = 2
scissors = 3
Sc1 = 0
Sc2 = 0
playing = True

print("Rock, Paper, Scissors")

print("Player 1, please enter your name: ")
Player1 = input()

print("Player 2, please enter your name: ")
Player2 = input()

def election():
    global Sel1, Sel2
    print("rock = 1"'\n'
        "paper = 2"'\n'
        "scissors = 3")
    print(Player1 + ", please enter your object: ")
    Sel1 = int(input())
    print(Player2 + ", please enter your object: ")
    Sel2 = int(input())
    return(Sel1, Sel2)

def play_again():
    if playing:
        print("Do you want to play again? (y/n)")
        if input() == "y":
            election()
            play(Sel1, Sel2)
        else:
            return("Thanks for playing!")

def score():
    print(play(Sel1, Sel2))
    print(Player1 + " score: " + str(Sc1))
    print(Player2 + " score: " + str(Sc2))
    play_again()

def compare(Sel1, Sel2):
    global Sc1, Sc2
    if (Sel1 == Sel2):
        return("It's a tie!")
    elif (Sel1 == 1):
        if (Sel2 == 3):
            Sc1 = Sc1 + 1
            return("Rock wins!")
        else:
            Sc2 = Sc2 + 1
            return("Paper wins!")
    elif (Sel1 == 3):
        if (Sel2 == 2):
            Sc1 = Sc1 + 1
            return("Scissors win!")
        else:
            Sc2 = Sc2 + 1
            return("Rock wins!")
    elif Sel1 == 2:
        if Sel2 == 1:
            Sc1 = Sc1 + 1
            return("Paper wins!")
        else:
            Sc2 = Sc2 + 1
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered"'\n'
              "1 = rock"'\n'
              "2 = paper"'\n'
              "3 = scissors"'\n'
              "try again.")

def play (Sel1, Sel2):
    if playing and (Sel1 == 1 or Sel1 == 2 or Sel1 == 3) and (Sel2 == 1 or Sel2 == 2 or Sel2 == 3):
        print(compare(Sel1, Sel2))
        print(score())
        print(play_again())

election()
play(Sel1, Sel2)