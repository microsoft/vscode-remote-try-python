#Repeating Execution
#Loop / Iteraton
#while : 只要是TRUE， 会一直运行
# increment： 
#x = x + 1  (x += 1)
#x = x - 1  (x -= 1)



# ans = input("Enter an integer: ")
# a = int(ans)
# b = 1
# while b <= 12:
#     print(a, "x", b, "=", a+b)
#     ans = ("Keep going?(y/n)")
#     if ans != 'y':
#         break
#     if b == 12:
#         break
#     b += 1

# while True:#ask for done, if no done, then, repeat
#     ans = input("Enter some text or 'done'>")
#     if ans != 'done':
#         print("you entered '" + ans + "' ")
#     else:
#         break


# enter a num, guess if num = random number
# import random
# pick = random.randint(1,3)
# total = 0
# correct = 0
# while True:
#     guess = input("Input a number or 'q' to quit:")
#     if guess == 'q':
#         break

#     guess = int(guess)
#     if guess == pick:
#         correct += 1
#         total += 1
#         print("Correct")
#         print(correct)
#         print(total)
#     else:
#         total += 1
#         print("wrong")
#         print(total)
# print(correct/total)


# continue
# count = 0
# while True:
#     name = input("name")
#     if name == " ":
#         continue
#     print("hello", name)
#     count += 1
#     ans = input("another friend? [y/n]")
#     if ans != 'y':
#         break
# print(count,"friends")

# Boolean variable
#ex. A = False

# import random
# pick = random.randint(1,100)

# while True:
#     ans = int(input("Enter a guess ")

#     if ans == pick:
#         print("Correct")
#         break
#     elif ans > pick:
#         print("TOO high")
#     else:
#         print("Too low")


#Formatting Floating point
# "{:.2f}".format#.2f : two float points
# n = 3.3365434
# a = "{:.2f}%".format(n)# %可加可不加
# print(a)

#another way to use print statement : sep=" " / end = " "
# print(1,2,3,sep="yy",end="oo")



# done = False

# while not done: #while True
#     print("spam.")
#     ans = input("Stop the spam?")
#     if ans == "y":
#         done = True


#Factorial 
# n = int(input("num"))
# def fact(n):
#     while True:
#         if (n ==1):
#             return 1
#         else:
#             return n *fact(n-1)
# fact(n)

# print(fact(n))
        
print(round(3.5))
    
