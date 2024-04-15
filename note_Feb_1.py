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
#     ans = int(input("Enter a guess "))
    

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


# #Factorial 
# n = int(input("num"))
# def fact(n):
#     while True:
#         if (n ==1):
#             return 1
#         else:
#             return n *fact(n-1)
# fact(n)

# print(fact(n))
        
        
    

# balance = 100
# yearly_rate = 7

# year = 1
# while year <50:
#     interest = balance * (yearly_rate/100)
#     balance = balance + interest
#     year = year +1
# print("After", year, "year, you have", "${:.2f}".format(balance))

#statistic program

# running_count = 0
# running_sum = 0
# running_min = None #emphasis the data is empty
# running_max = None

# while True:
#     ans = input("Enter a number or 'done'")

#     if ans == 'done':
#         break

#     num = float(ans)
#     #update the statistic
#     running_count = running_count +1

#     running_sum = running_sum + num

#     if running_min == None or num < running_min:
#         running_min = num

#     if running_max == None or num > running_max:
#         running_max = num


# print(running_count)
# print(running_sum)
# print(running_min)
# print(running_max)

# #nested loop
# row = 1
# while row < 12:
#     col = 1
#     row += 1
#     print("6", end="")
#     print()
#     while col <= 12:
#         print("6", end="")
#         col += 1

# hours = 0
# minutes = 0
# while True:
#     if minutes <= 60:
#         minutes = minutes + 1
#         print(minutes)
#     if minutes == 60:
#         hours = hours + 1
#     minutes = 0
#     break


    # else:
    #     minutes = minutes + 1
    #     hours = hours + 1
    #     minutes = 0
    #     minutes = 1

# print(i)
# # while i < 600:
# #            print('Goodbye')
# #            i = i + 1
# # print(i)
 
# print(500//67)
# print(500%67)

# print("Pi day sale!")
# pi = 3.14159262
# print("All pies","${:.2f}".format(pi),"off.")

# ans = input("Exit?")
# while ans == "n":
#    ans = input("Exit?")

# running_sum = 0
# while True:
#     score = input("Enter a test score or 'exit':") 
#     if score == 'exit':
#         break
#     score = float(score)
#     if score >= 0 and score <= 100:
#         running_sum += score
#         continue
# print("The total is", running_sum)


# x = int(input("Enter a positive double digit integer:"))
# while x <= 10 or x >= 99:
#     x = int(input("Enter a positive double digit integer:"))
# print("You chose", x)

# n = int(input("enter a maximum number n:"))
# while True:
#     if n > 0:
#         n = n/10
#         print(n)
# n = int(input("Enter a number (n): "))
# i = 10

# while i < n:
#     print(i)
#     i += 10

# j = 5
# while j > 0:
#     k = 1
#     while k <= j :
#         print("#", end = "")
#         k = k + 1
#     print()
#     j = j - 1


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # index operator: [] 里面必须是integer
# # ex. 
# text = "hello world"
# print(text[0]) 
# # >>> H
# print(text.find('h'))
# # >>> 0
# print(len(text))
# print(text[len(text)-1])
# # >>> d
# i = 0
# while i < len(text):
#     print(text[i])
#     i += 1


# #same as the method above
# for c in text: # for every 
#     print(c)


# #same as the method above
# for i in range(len(text)):
#     print(text[i])

# -1 右到左第一个。   1: 左到右第一个
# text = "spoon and fork"
# print(text[0:3] + text[12:14])
# print(text[10:15])
# print(text[-1])
# print(text[5:])
# # >>> and fork
# print(text[:5])
# # >>> spoon
# print(text[1:])

# # ord("")
# print(ord("A"))
# print(ord("a"))

# # .upper()
# print("apple".upper())
# #>>> APPLE


# print("H" in text)# >>> False
# print("s" in text) # >>> True

# print(text.find("spoon") >= 0)# >>> True
# print(text.find("help") >= 0)# >>> False

# # print(dir(text))
# # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
# #  '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', 
# #  '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
# #    '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# #      'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
# #        'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 
# #        'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
# #        'translate', 'upper', 'zfill']
# title = "welcome to ucd"
# print(title.capitalize())
# print(title.title()) 


# email = "tea@ucdavis.edu"
# print(email.find("@", 3)) # >>> 3 # Exist
# print(email.find("@", 5)) # >>> -1 # DNE

# # replace
# print(title.replace('welcome', 'KIMI')) 
# # >>> KIMI to ucd

# print(title.replace('welcome', '')) 
# # >>> to ucd


# #strips

# line = "     happy new year\n"
# print(line)
# print(line.strip())


# lines = "$20.445"
# lines = lines.strip("$")
# print(lines)
# float(lines)#strip 后就可以 convert str to int

# #split
# print("do,re/mi,fa".split("/"))

# #
# word = input("ENter words: ")

# running_length = 0
# num_vowels = 0
# num_cons = 0
# num_upper = 0
# num_lower = 0

# for char in word:
#     running_length = running_length +1
#     if char.isupper():   
#         num_upper += 1
#     if char.islower():
#         num_lower += 1
#     if char in 'aeiou':
#         num_vowels += 1
#     else:
#         num_cons += 1
# print(num_vowels,num_cons,num_cons,num_upper,num_lower)


# #reverse
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#open file
# infile = open("file.form")
# outfile = open("song.txt","w")

#w = write
#a = append
#r = reading

# write = print # only take one input, one string

# outfile.write(line)
# line = infile.readline()
# outfile.close()

# program: write_song.py
# open a file handle for writing
# outfile = open("song.txt","w")

# line = "ho si hei die o"
# line = line + "\n"
# outfile.write(line)# wirte only  take one string

# line = "niu bi 666"#向文件中添加歌词
# outfile.write(line+ "\n")

# outfile.close()

# program 2
# import random
# num_lines = int(input("How many numbers to write?"))
# largest = float(input("Largest number"))
# filename = input("Output filename")

#open file
# outfile = open(filename,"w")

#generate num_lines random numbers and write them to output file

# for line_num in range(num_lines):
#     num = random.random()
#     num *= largest
#     line = str(num) + "\n"
#     outfile.write(line)
# outfile.close()


# # Program: read_num.py
# filename = input("file name: ")
# infile = open(filename)
# for line in infile:
#     # line = line.strip()
#     print(line)


# #statistic_file.py
# while True:
#     try:
#         filename = input("file name: ")
#         infile = open(filename)
#         break
#     except:
#         continue

# running_sum = 0
# cunning_count = 0
# running_max = 0
# running_min = 0
# for line in infile:
#     line = line.strip()
#     num = float(line)
#     cunning_count += 1
#     running_sum += num 
#     if running_max == None or num > running_max:
#         running_max = num
#     if running_min == None or num < running_min:
#         running_min = num
# print("Number of data items: ",cunning_count)
# print("Average: ",running_sum/cunning_count)
# print("Max: ", running_max)
# print("Min: ", running_min)


# #program : starbucks_menu.py

# filename = input("file name: ")
# infile = open(filename)

# line = infile.readline()
# min_carbs = None
# max_cals = None
# min_item = None
# max_item = None

# for line in infile:
#     line = line.strip()
#     items, cals, carbs = line.split("\t")
#     cals = int(cals)
#     carbs = int(carbs)

#     if min_carbs == None or carbs < min_carbs:
#         min_carbs = carbs
#         min_item = items
#     if max_cals == None or cals > max_cals:
#         max_cals = cals
#         max_item = items
# print("Max cals: ", max_cals)
# print("Min Carbs: ", min_carbs)
# print("min items: ", min_item)
# print("max items: ", max_item)

# #strip string
# line = "hello Bagal\t\t50"
# line.strip()

# #program: write_csv.py
# filename = "names.csv"
# outfile = open(filename,"w")

# while True:
#     first = input("Enter first and last name or nothing to exit: ")
#     if first == "":
#         break
#     first, last = .split()
#     line = last + "," + first, "\n"
#     outfile.write(line)

# outfile.close()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ####list
pets = ['dogs', 'lion', 'cat','rabbit','whale']

# print(pets[0])#first from left
# print(pets[-1])#first from right
# print(pets)#print whole list

# pets[0] = "happy"
# print(pets)#替换第一个index

# pets[0] = pets[0] + "666"
# print(pets)#修改第一个index

# ####append
# #list.append(填充物)
# pets.append("rabbit")
# print(pets)# 添加rabbit 为pets[4]

# ####number in list
# numbers = [1,2,3,4]

# ####create a empty list
# list = []

# #list can contain mixed data type
# item1 = ["Bagel", 500]
# item2 = ["Muffin", 400]
# item3 = ["Criossant", 430]
# menu = [item1,item2,item3]
# print(menu)
# print(menu[1][0]) # item2, index1

# number = []
# for i in range(1,10,2):
#     number.append(i)
#     print(number)

# # for i in pets: # i : element in list
# #     print(i)
# #     print(i + "s")

# for i in range(0,len(pets)):
#     pets[i] += "s"
#     print(pets[i])

# for i in range(len(number)):
#     number[i] = number[i]**2
#     print(number[i])


####List method and Functions
#read_names.csv program
# filename = input(" Enter filename: ")

# infile = open(filename)

# for line in infile:
#     line = line.strip()
#     cols = line.split(",") #把cols换成first， last， result ！= list
#     print(cols) #>>> list

    # last = cols[0]
    # first = cols[1]
    # print(first, last)


# ####pop
# # pets = ['dogs', 'lion', 'cat','rabbit','whale']
# print(pets.pop())
# print(pets.pop(0))

# ####sort 

# pets = pets.sort(reverse=True)
# print(pets)

# num = [2,4,3,5,6,7,4,6]
# print(sorted(num))

# statistics_lust.py
# nums = []
# filename = input("Enter the filename: ")
# infile = open(filename)

# for line in infile:
#     line = line.strip()
#     num = float(line)#没有这个就是string
#     nums.append(num)
# print("Count", len(nums))
# print("Max", max(nums))
# print("min", min(nums))
# print("total", sum(nums))
# print("avg", sum(nums)/len(nums))

# nums = [1,2,3,4]
# if len(nums) % 2 != 0:
#     median = nums[len(nums)//2]
# else:
#     midian = ((nums[len(nums)/2] + nums[(len(nums)/2)-1])/2)

# import random          
# file = open("random.txt","w")

# for i in range(0,10):
#     num = str(random.random()*10) + "\n"

#     file.write(num)


# file.close()
# list = []
# file = open("random.txt","r")
# for i in file:
#     i = i.strip()
#     i = "{:.1f}".format(float(i))
#     list.append(i)

# print(list)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# nums = []
# for num in range(1,100,2):
#     nums.append(num)
# print(nums)
# print(nums[0:11])
# print(nums[:3])
# print(nums[-3:])
# num2 = nums
# nums = nums[:]
# print(sorted(num2))
# print(num2.sort(reverse = True))

# s = "hello"
# print(s[0:3]) 

# word = "hypothesis"
# print(min(word))
# print(max(word))
# print(sorted(word))

# num3 = nums + num2
# print(num3)


# filename = input("input filename: ")
#////////////////////////////////////////////////////////////////////////////////////////////////////////
#function 
# parameter = variable
#function = value

#fruitful returns value
#void function doesn't return value
# function must be called
def cube(x):
    ans = x*x*x
    return ans

y = cube(3)

print(y)


def greet_user(user):
    result = user + "!"
    return result
a = input("name")
print(greet_user(a))


# def get_email():
#     while True:
#         email = ("Enter an email:")
#         if email.count("@") == 1:
#             break
#         else:
#             print("Not a valid email")
#     return get_email
# print(get_email())

def can_be_int(s):
    try:
        int(s)
        return True
    except:
        return False
print(can_be_int("3.13"))
print(can_be_int("3"))

ans = input("enter a value")

if can_be_int(ans): #if input is a int
    print("That is a integer")
else: # if not a int
    print("not a integer")


#/////// split("")
a = "kimiyuzhezheng@gmail.com".split("@")
print(a)
#>>> ['kimiyuzhezheng', 'gmail.com']


# unfinished program 
email = input("enter email: ")
def get_email_parts(email):
    user, domain = email.split("@")
    return user, domain

email = get_email_parts(email)
user, domain = get_email_parts()

###
def sort_list(L):
    L.sort()
    for item in L:
        print(item)

pets = ["A", "Z", "O", "F"]
print(sort_list(pets))

    



    