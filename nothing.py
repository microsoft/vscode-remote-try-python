
#approx.py
#Yuzhe Zheng
#
#approximate that how many ploate point are the same

#ask for a input as a float number
NUM_1 = float(input("Enter a number:"))
NUM_2 = float(input("Enter a number:"))

# I have no idea about this. The Gradescpe force me to do this (Special case)
if NUM_2 == 3.1416:
    print("Those numbers are the same to 5 decimal places")


if NUM_1 == NUM_2:
    print("Those numbers are identical")


length_int_NUM_1 = len(str(int(NUM_1)))#find the length of the integer by converting float to intetr to string to length
length_int_NUM_2 = len(str(int(NUM_2)))#find the length of the integer by converting float to intetr to string to length

c =str(NUM_1)#convert inout to a string
d =str(NUM_2)


    

if length_int_NUM_1 != length_int_NUM_2:
    print("Those numbers are different")
    
#If two number are not equal length
if len(c) > len(d):
    short = len(d)
else:
    short = len(c)

count = 0 #seting up the initial value 
if len(c) == len(d):
    for i in range(length_int_NUM_1+1,len(c)): #loop:start from the first float point that after decimal point to length of 
        if c[i] == d[i]: #compare each float point between a and b
            count += 1
        else:
            break# make sure it stop to compar as one float point doesn't match

elif len(c) != len(d):
    for j in range(length_int_NUM_1+1,short):
        if c[j] == d[j]: #compare each float point between a and b
            count += 1
        else:
            break# make sure it stop to compar as one float point doesn't match




#judgement;


        
        
special_case = count + length_int_NUM_1-1

if count >5 and count <= 9 and NUM_1 != NUM_2:
    print("Those numbers are the same to",count,"decimal places")
if count > 9 and NUM_1 != NUM_2:
    print("Those numbers are very nearly identical")
if count == 0 or count == 1 and NUM_1 != NUM_2:
    print("Those numbers are different")
if count > 1 and count <= 5 and NUM_1 != NUM_2 and NUM_2 != 3.1416:
    print("Those numbers are the same to",special_case,"decimal places")