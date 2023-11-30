#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


def get_oponent_options():
    options = ["piedra", "papel", "tijeras"]
    return random.choice(options)

def get_result(player, oponent):
    if player == oponent:
        return "Empate"
    elif player == "piedra" and oponent == "papel" or player == "papel" and oponent == "tijeras" or player == "tijeras" and oponent == "piedra":
        return "Perdiste"
    else:
        return "Ganaste"
    
def play():
    wins = 0
    rounds = 0

    while True:
        player = input("Elige piedra, papel o tijeras: ").lower()

        if player not in ["piedra", "papel", "tijeras"]:
            print("Opcion incorreta. Elige de nuevo")
            continue

        oponent = get_oponent_options()
        result = get_result(player, oponent)

        print(f"Tú elegiste {player}, el oponente eligió {oponent}. Resultado: {result}")

        rounds += 1
        if result == "Ganaste":
            wins += 1

        play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if play_again != "s":
            break

    print(f"Juego terminado. \nJugaste {rounds} rondas. Ganaste {wins} rondas.")


if __name__ == "__main__":
    print ("Bienvenido a Piedra, Papel o Tijera")
    play()




