#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
# write 'hello world' to the console
print("hello world")

def play_game():
    options = ["rock", "paper", "scissors"]
    player_score = 0
    opponent_score = 0

    while True:
        player_choice = input("Elige una opción (rock, paper, scissors): ").lower()

        if player_choice not in options:
            print("Opción no válida. Por favor, elige entre rock, paper o scissors.")
            continue

        opponent_choice = random.choice(options)
        print("El oponente eligió:", opponent_choice)

        if player_choice == opponent_choice:
            print("Empate!")
        elif (player_choice == "rock" and opponent_choice == "scissors") or \
             (player_choice == "scissors" and opponent_choice == "paper") or \
             (player_choice == "paper" and opponent_choice == "rock"):
            print("¡Ganaste!")
            player_score += 1
        else:
            print("Perdiste.")
            opponent_score += 1

        play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if play_again != "s":
            break

    print("Puntuación final:")
    print("Jugador:", player_score)
    print("Oponente:", opponent_score)

play_game()
