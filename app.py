#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return app.send_static_file("index.html")

#print player score at the end
user_score=0
user=input();   
user=user.lower();
import random
computer=random.choice(['rock','paper','scissor'])
print(computer)
if user==computer:
    print("tie")
elif user=='rock':
    if computer=='paper':
        print("computer wins")
    else:
        print("user wins")
        user_score+=1
elif user=='paper':
    if computer=='scissor':
        print("computer wins")
    else:
        print("user wins")
        user_score+=1
elif user=='scissor':
    if computer=='rock':
        print("computer wins")
    else:
        print("user wins")
        user_score+=1
else:
    print("invalid input")
while True:
    user=input("do you want to play again? (y/n)");
    if user=='y':
        user=input("enter your choice: rock,paper or scissor");
        user=user.lower();
        import random
        computer=random.choice(['rock','paper','scissor'])
        print(computer)
        if user==computer:
            print("tie")
        elif user=='rock':
            if computer=='paper':
                print("computer wins")
            else:
                print("user wins")
                user_score+=1
        elif user=='paper':
            if computer=='scissor':
                print("computer wins")
            else:
                print("user wins")
                user_score+=1
        elif user=='scissor':
            if computer=='rock':
                print("computer wins")
            else:
                print("user wins")
                user_score+=1
        else:
            print("invalid input")
    else:
        break
