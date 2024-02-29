# # parrot.py
# # Yuzhe Zheng

# # upper case 
# # while True: # infinity loop
# #     n = input() # ask inout
# #     if n == 'quiet': # hit quirt then quit
# #         break
# #     else:
# #         print(n.upper())# convert every inout to upper case

# #passward.py
# #Yuzhe Zheng
# #
# #use increment to check the existence of lower, upper cases, digital, and special
# password = input("Enter password ")
# lower_case = 0 # initialize the value * 4
# upper_case = 0
# digit = 0
# special = 0
# for char in password:# go though every character in input
#     if char.islower():# check if the char is in lower case
#         lower_case += 1 # increment
#     elif char.isupper():# check if the char is in upper case
#         upper_case += 1# increment
#     elif char.isdigit():# check if the char is digit
#         digit += 1# increment
#     if char == '!' or '@' or '#' or '$' or '%' or'&':
#         special += 1
# # except the length which the chars number need to greater than 8, others only need to exceed 1
# if len(password) >= 8:
#     print("Has length")
# if lower_case > 0:
#     print("Has lower case")
# if upper_case > 0:
#     print("Has upper case")
# if digit > 0:
#     print("Has digit")
# if special > 0:
#     print("Has special")


# #phone.py
# #Yuzhe Zheng
# #
# #Use index operator to limit the form of phone number

# n = input("Enter number as ### ###-####:")
# if len(n) == 12:# the length of phone number is 12
#     #make sure the phone number made by 3 nums ,3nums ,- ,4nums.
#     if n [0:2].isalnum() and n[4:6].isalnum() and n[7] == "-" and n[8:11].isalnum():
#         print("Valid")
# else:
#     print("Invalid")
        
# #digits.py
# #Yuzhe Zheng
# #
# #print out phone number and get rid off - and ()
# n = input("Enter phone number:")
# print("Digit string: ", end = "")# this must be outside of the loop, and keep in same time with the phone number
# for char in n:# check every char in phone number
#     if char.isalnum():# check if char is a number 
#         print(char, end="") # print out every number and keep at the same line with the last print statement



# #cat.py
# #Yuzhe Zheng
# #
# #open file
# file_name = input("Enter a file name to open:")# ask file name
# file = open(file_name,"r") # open file as read mode 
# for char in file: # print our each char in song
#     print(char, end= "") # delete the gap empty line


# #trycat.py
# #Yuzhe Zheng
# #
# # use try and except to eliminate the error the pointed out by system
# file_name = input("Enter a file name to open:")
# while True:
#     try:# if True
#         file = open(file_name,"r") # open file as read mode
#         for char in file:# print every char in file
#             print(char, end= "")
#         break# just print one time
#     except:# otherwise
#         print("Could not open", "'"+file_name+"'")
#         break


# #cash.py
# #Yuzhe Zheng
# #
# #sum up all the number in the file
# sum = 0 # initialize the total
# print("Automated cash register")

# file_name = input("Enter a file name to open:") # ask for file name
# file = open(file_name,"r")# open file as read mode

# for num in file: # go though every number in the file
#     num = float(num) # convert str to float
#     sum += num # increment
# print("File contained 3 items totaling: $"+str(sum))
    

# #cash2.py
# #Yuzhe Zheng
# # 
# #
# #sum up all the number in the file
# sum = 0 # initialize the total
# print("Automated cash register")

# file_name = input("Enter a file name to open:") # ask for file name
# file = open(file_name,"r")# open file as read mode

# for num in file: # go though every number in the file
#     while True: # loop
#         try:
#             num = num.strip("$") # get rid off dollar sign
#             if num.isalpha(): # skip the line that do do contain number
#                 continue
#             num = float(num) # convert str to float
#             sum += num # increment
#             break# stop 
#         except:
#             break
# print("File contained 3 items totaling: $"+str(sum))






# n = input("Enter your 8-digit card number:")

# n = n.replace(" ","")
# sum = 0
# SUM = 0
# print(len(n))
# # initial 8-digits case:
# #-1 -3 -5 -7
# for num in range(0,-4,-1):
#     num = int(num)
#     R_1 = n[2*num -1]
#     sum += int(R_1)
# #0 2 4 6 8
# for NUM in range(0,4,1):
#     NUM = int(NUM)
#     R_2 = n[2*NUM]
#     SUM += 2 * int(R_2)
    
# total = sum + SUM
# if total % 10 == 0:
#     print("Valid")
# elif total % 10 != 0:
#     print("Invalid")
    



# if 1234 567 =>  len = 4

# length = len(n)
# if total % 10 != 0:
#     while length > 0:
#         length -= 1
#         for num in range(0,round(-length/2),-1):
#             num = int(num)
#             R_1 = n[2*num -1]
#             sum += int(R_1)
#             #print(R_1)

#         for NUM in range(0,4,1):
#             NUM = int(NUM)
#             R_2 = n[2*NUM]
#             SUM += 2 * int(R_2)





# #0123 4567  
# #abcd gfdh
# #-8,-7,-6,-5, -4,-3,-2,-1
# #2(a+c+g+d) + (d+b+f+h) % 10 = 0

    

        
        

    
    
    









# # SUM = int(n[1]) + int(n[3]) + int(n[6]) + int(n[8])
# # sum = (int(n[0]) + int(n[2]) + int(n[5]) + int(n[7]))*2
# # total = SUM + sum
# # if total % 10 == 0:
# #     print("Valid")
# # else:
# #     print("Invalid")
# #     print("Check digit should be")



# #cash.py
# #Yuzhe Zheng
# #
# #sum up all the number in the file
# sum = 0 # initialize the total
# count = 0
# print("Automated cash register")

# file_name = input("Enter file of prices:") # ask for file name
# file = open(file_name,"r")# open file as read mode

# for num in file: # go though every number in the file
#     try: # convert to float if it is convertible
#         num = num.strip('$')#get rid off $
#         num = float(num) # convert str to float
#         sum += num # increment
#         count += 1# update count
#     except: 
# #         continue
# # print("File contained", count, "items totaling ${:.2f}".format((sum)))
# n = input("Enter your 8-digit card number:")

# n = n.replace(" ","")
# sum = 0
# SUM = 0
# print(len(n))
# # initial 8-digits case:
# for num in range(0,-4,-1):
#     num = int(num)
#     R_1 = n[2*num -1]
#     sum += int(R_1)

# for NUM in range(0,4,1):
#     NUM = int(NUM)
#     R_2 = n[2*NUM]
#     SUM += 2 * int(R_2)
    
# total = sum + SUM
#parrot.py
#Yuzhe Zheng
#
# #upper case
# while True: # infinity loop
#     n = input(">") # ask inout
#     n = n.lower()
#     if n == 'quiet': # hit quirt then quit
#         break
#     else:
#         print(n.upper())# convert every inout to upper case


# #digits.py
# #Yuzhe Zheng
# #
# #print out phone number and get rid off - and ()
# n = input("Enter phone number:")
# # for each of the special characters in the list
# for c in [")","(","-"," "]:
#     # replace that character with an empty string
#     n = n.replace(c,"")

# # print result
# print("Digit string:",n)


# while True:
#    fname = input("Enter a filename:")
#    try:
#        fhand = open(fname)
#    except:
#        continue
#    break


# s = input("Enter a price:")
# try:
#     if float(s.strip("$")) - float(s.strip("$")) == 0 or float(s) - float(s) == 0 :
#         price = "{:.1f}".format(float(s.replace("$","")))
#     print("Price as float:", price)
# except:
#     print("That's not a price!")

n = input("Enter your 8-digit card number:")

n = n.replace(" ","")
sum = 0
SUM = 0
# initial 8-digits case:

for num in range(0,-4,-1):# Order from right to left
            
    num = int(num)#convert str to int
    R_1 = n[2*num -1]#chose the right most and skip one and chose one
    sum += int(R_1)# update the sum

for NUM in range(0,4,1):# Order from left to right

    NUM = int(NUM)
    R_2 = int(n[2*NUM])
    R_2 = 2*R_2
    
    
    if R_2 >= 10:
        partial_sum = 1 + (R_2 - 10)
        SUM += partial_sum
    elif R_2 < 10:
        SUM += R_2

print(sum)
print(SUM)

total = sum + SUM
print(total)

if total % 10 == 0:
    print("Valid")
elif total % 10 != 0:
    print("Invalid")

if total % 10 != 0:
    total = str(total)
    rest = 10 - int(total[1])
    print(rest)
    if int(n[7])+rest < 10:
        print("Check digit should be ",int(n[7])+rest)
    elif int(n[7])+rest > 10:
        i = int(total) % 10
        left = (int(n[7])-i)
        print("Check digit should be ",left)
       
        
        
        



    

    


