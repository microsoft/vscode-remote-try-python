##### #23日 2 月 2024 年################################################################################################################

#Even 

# x = int(input("NUM"))
# if x % 2 == 0:
#     print("Even")
# if x % 2 == 1:
#     print("odd")

#if
#else if
#elif : every condition fail
# if = elif > else

##### #25日 2 月 2024 年################################################################################################################

# ans = "y"
# if ans =="y":
#     raining = True
# else:
#     raining = False

#replaceble (18 - 21 row)
# raining = ans == "y"

#random Number

# import random 
# A = random.randint(0,36)
# print(A)

# print(random.random())#give a random float number between 0 to 1

# B = random.choice(["Tim", "Tasty", "Davis", "Somewhereelse"])#:random get a element from the []
# print(B)

# #eval() = evaluation
# #take the string to calculate
# #ex. 
# print(eval("2 - 2")) # >>>0 


# # #:initialized random value

# print(99%2)
# print(80%2)

# annual_rate = 7.0 # annual interest rate
# monthly_rate = annual_rate/12
# balance = 100 # account balance
# month = 1 # current month
# # loop for 50 years updating balance
# while balance <=1000000:
#     interest = balance*0.07
#     balance = balance + interest
#     month = month + 1
# formatted = "${:.2f}".format(balance)
# print("In 50 years you'll have",formatted)

##### 6 / Feb / 2024 ################################################################################################################
# Mid-Term: only use the sources from textbook!!!

        #. <<for loop>>

# for i in [2, 4, 3, 5, 1]: # sequence of value
#     print(i, sep = "\t", end =" ")
# # >>>2 4 3 5 1 

# for j in range(0,10,1): 
#     print(j, sep = "\t", end =" ")


# for day in ['mon', 'tue', 'wed', 'thu', 'fri', 'sat','sun']:
#     print("working on ", day)

# value = [3,1,4,1,5,9,2,6,5,3,5]
# print(sum(value))
# print(len(value))

# # 九九乘法表
# for row in range(1,9):
#     for col in range(1,10):
#         print("{:4.0f}".format(row*col),end= "") # "{:4.0f}" 4:间距4 
#     print()#goto next line after printing one line

# #pythagorean triples

# #Brute force computation
# count = 0
# for a in range(1,101):
#     for b in range(a+1,101):
#         for c in range(b+1,101):
#             if a**2 + b**2 == c**2:
#                 print(a,b,c)
#                 count += 1
# print("count: ",count)


# <<try and except>>

#check if the input is valid
# import sys
# while True:
#     user = input("temp")
#     try:
#         user = float(user)
#     except:
#         print("no")
#         sys.exit()
#     if user > 0: #在转化成数字后，退出
#         break
#     else:
#         print("no num")



# print(user/3)

while True:
    try:
        filename = input("Enter the file name:")
        open(filename)
        break
    except:
        print("DNE")
        












