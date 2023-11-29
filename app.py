#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
from pick import pick
import random

app = Flask(__name__)

rounds = 0
user_wins = 0
computer_wins = 0

hands = [
    {"name": "🪨 Piedra", "beat": [{"name": "✂️ Tijera", "lore": "Piedra aplasta tijeras"}, {"name": "🦎 Lagarto", "lore": "Piedra aplasta lagarto"}]},
    {"name": "📜 Papel", "beat": [{"name": "🪨 Piedra", "lore": "Papel cubre piedra"}, {"name": "🖖 Spock", "lore": "Papel desaprueba Spock"}]},
    {"name": "✂️ Tijera", "beat": [{"name": "📜 Papel", "lore": "Tijeras cortan papel"}, {"name": "🦎 Lagarto", "lore": "Tijeras decapitan lagarto"}]},
    {"name": "🦎 Lagarto", "beat": [{"name": "🖖 Spock", "lore": "Lagarto envenena Spock"}, {"name": "📜 Papel", "lore": "Lagarto come papel"}]},
    {"name": "🖖 Spock", "beat": [{"name": "✂️ Tijera", "lore": "Spock destruye tijeras"}, {"name": "🪨 Piedra", "lore": "Spock vaporiza piedra"}]}
    ]

@app.route("/")
def hello():
    return app.send_static_file("index.html")

def menu():
    global rounds, user_wins, computer_wins

    print("\033c")
    title = "🫡 Bienvenido a Piedra, Papel, Tijera, Lagarto o Spock"
    options = ["🎮 Jugar" if rounds == 0 else "🎮 Jugar Revancha"]
    options.append("📝 Ver Reglas")
    options.append("🚪 Salir")

    option, index = pick(options, title, indicator='👉')

    if index == 0: play()
    elif index == 1: rules()
    elif index == 2: exit()

def play():
    global rounds, user_wins, computer_wins, hands
    
    title = "🎮 ¿Qué elijes? 🎮"
    options = [hand["name"] for hand in hands]
    option, index = pick(options, title, indicator='👉', default_index = 2)

    user_choice = index
    computer_choice = random.randint(0, 4)

    print("\033c")
    print("👤 Usuario: " + options[user_choice])
    print("🤖 Computadora: " + options[computer_choice] + "\n")

    if user_choice == computer_choice:
        print("🤝 Empate")
    else:
        if hands[user_choice]["name"] in [beat["name"] for beat in hands[computer_choice]["beat"]]:
            print("🤖 " + hands[computer_choice]["beat"][0]["lore"] if hands[computer_choice]["beat"][0]["name"] == hands[user_choice]["name"] else hands[computer_choice]["beat"][1]["lore"])
            computer_wins += 1
        else:
            print("👤 " + hands[user_choice]["beat"][0]["lore"] if hands[user_choice]["beat"][0]["name"] == hands[computer_choice]["name"] else hands[user_choice]["beat"][1]["lore"])
            user_wins += 1

    rounds += 1
    print("\n👤 Victorias de Usuario: " + str(user_wins))
    print("🤖 Victorias de Computadora: " + str(computer_wins))
    print("🔢 Ronda: " + str(rounds))
    input("Pulsa una tecla para continuar...")
    menu()

def rules():
    print("📝 Reglas del juego 📝\n")
    print("✂️ -> 📜 (Tijeras cortan papel)")
    print("📜 -> 🪨 (Papel cubre piedra)")
    print("🪨 -> 🦎 (Piedra aplasta lagarto)")
    print("🦎 -> 🖖 (Lagarto envenena Spock)")
    print("🖖 -> ✂️ (Spock destruye tijeras)")
    print("✂️ -> 🦎 (Tijeras decapitan lagarto)")
    print("🦎 -> 📜 (Lagarto come papel)")
    print("📜 -> 🖖 (Papel desaprueba Spock)")
    print("🖖 -> 🪨 (Spock vaporiza piedra)")
    print("🪨 -> ✂️ (Piedra aplasta tijeras)")
    input("\nPulsa una tecla para continuar...")
    menu()

if __name__ == "__main__":
    menu()