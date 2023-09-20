#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")

# write a game which plays rock paper and scissor game through console with user

def play_game():
    print("Bem Vindo ao jogo Jokempô")
    print("Escolha uma das opções")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    user_choice = int(input("Digite sua opção: "))
    print("Sua opção foi: ", user_choice)
    print("Computados está escolhendo...")
    import random
    computer_choice = random.randint(1, 3)
    print("Computador escolheu: ", computer_choice)
    if user_choice == computer_choice:
        print("Empatou")
    elif user_choice == 1 and computer_choice == 2:
        print("Computador ganhou")
    elif user_choice == 1 and computer_choice == 3:
        print("Você ganhou")
    elif user_choice == 2 and computer_choice == 1:
        print("Você ganhou")
    elif user_choice == 2 and computer_choice == 3:
        print("Computador ganhou")
    elif user_choice == 3 and computer_choice == 1:
        print("Computador ganhou")
    elif user_choice == 3 and computer_choice == 2:
        print("Você ganhou")
    else:
        print("Opção inválida")

play_game()



