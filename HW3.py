# #pocket
# #Yuxhe Zheng
# #
# #change money
# print("Compute your pocket change!")
# Q = int(input("Quarters?"))#get input and convert string to integer
# D = int(input("Dimes?"))#get input and convert string to integer
# N = int(input("Nickels?"))#get input and convert string to integer
# P = int(input("Pennies?"))#get input and convert string to integer
# print("The total is", "{:.2f}".format(Q*0.25+D*0.1+N*0.05+P*0.01))#convert result to 2 decimal places


# total = int(input("Enter cents:"))#convert input to a integer
# print("The minimum coins for",total,"cents are:")

# Quarters = total//25 #count how many Quarters in total
# rest_moneyMAX = total%25#count how many pennis in left
# Dimes = rest_moneyMAX //10#count how many Dimes in total
# rest_moneyMED = rest_moneyMAX % 10#count how many pennis in left
# Nickels = rest_moneyMED // 5#count how many Nickels in total
# rest_moneyMIN = rest_moneyMED % 5#count how many pennis in left
# Pennies = rest_moneyMIN // 1#count how many Pennis in total

# #print statement
# print(Quarters,"Quarters")
# print(Dimes,"Dimes")
# print(Nickels,"Nickels")
# print(Pennies,"Pennies")


# #dog
# #Yuzhe Zheng
# #
# #see if the weather and temp is appropreate to go outside with dog
# wea = input("Enter weather condition (rainy/sunny/snowy/cloudy):")
# tem = int(input("Enter temperature:"))
# print("Instructions for the walk:")
# if wea == "rainy" and tem > -14 and tem <=144:#range: tem > -14 and tem <=144
#     print("The dog should be taken for a short walk with an umbrella.")
# if wea == "snowy" and tem > -14 and tem <=144:#range: tem > -14 and tem <=144
#     print("Take the dog for a short walk and ensure they stay warm.")
# if wea == "cloudy" and tem > -14 and tem <=144:#range: tem > -14 and tem <=144
#     print("Enjoy a regular walk with your dog.")
# if wea == "rainy" and tem > -14 and tem <=144:#range: tem > -14 and tem <=144
#     print("Enjoy a regular walk with your dog.")
# if tem > 80 and tem <= 144 and wea == "sunny":#range: tem > 80 and tem <= 144
#     print("The dog should be taken for a walk in the shade and given water.")
# if tem > 45 and tem <= 80 and wea == "sunny":#range: tem > 45 and tem <= 80
#     print("The dog can enjoy a regular walk.")
# if tem > -14 and tem <= 45 and wea == "sunny":#range: tem > -14 and tem <= 45
#     print("Dress the dog warmly for a walk.")
# if tem != "rainy" or tem != "sunny" or tem != "snowy" or tem != "cloudy" or tem < -14 or tem >144:# Invalid statement
#     print("Invalid weather condition.")
    

# #tip
# #Yuzhe Zheng
# #
# #find tip
# total = float(input("Enter total:"))#get input and convert to float
# n = 0#set up initial value
# while n < 11:#while loop, looping 11 times
#     n += 1 #increment
#     print("A","{:.2f}%".format(14+n),"tip is ${:.2f}".format(total * ((14+n)/100)))#start from 15, then loop 10 times
#     #using "{:.2f}%".format() to get 2 decimal places after decimal point.




# #cash_register
# #Yuzhe Zheng
# #
# #find total cost
# n = 0#initialize the number of item
# total = 0#initialize the total
# print("Cash register (press enter to exit)")
# while True:
#     value = input("Enter item cost:")
#     if value == "":# if we press enter, then convert sting " " to int 0
#         value = 0
#         break
#     n += 1# increment of number of items
#     money = float(value) #if we enter number, convert number to float
#     total += money#sum up

# print("You entered",n,"items totaling", "{:.2f}".format(total))


# #roth
# #Yuzhe Zheng
# #
# #find how long it will take to make deposit double
# deposit = float(input("Enter an initial Roth IRA deposit amount:"))
# print("Enter an annual percent rate of return:15")
# years = 0#initialized the year
# total = deposit#set the initial deposit is the input number
# while total < 2*deposit:# keep running till double
#     years +=1 # count years
#     total += 0.15*total# 0.15 * initial deposit + initial deposit
#     print("Value after year", years, ": ${:.2f}".format(total))
# print("It will take", years, "years to double your investment with a 15% APR.")
        


# #car
# #Yuzhe Zheng
# #
# #guess the price of car
# print("Guess the price and win the prize!")
# n = 0# initialized the value
# while True:
#     n += 1# increment
#     price = int(input("Enter your guess:"))
#     if price == 44500 and n <= 5:# take 5 times and guess correctly, win
#         print("It took",n, "guesses.")
#         print("You won the car!")
#         break
#     if price == 44500 and n > 5:# although got correct answer, but still lose
#         print("It took",n, "guesses.")
#         print("Too many guesses!")
#         break

#     if price > 44500:# to see if the answer is too high or too low
#         print("Too high!")
#     if price < 44500:
#         print("Too low!")
   

# #mileage    
# #Yuzhe Zheng
# #
# #find ave. of Average mileage 
# total_m = 0
# total_g = 0
# print("Your Personal Fuel Economy")
# while True: # repeat questions
#     miles = input("Number of miles traveled (or enter to exit):")

#     if miles == "":# print result when hit enter
#         print("Average mileage =","{:.1f}".format(total_m /total_g))# formula of average
#         break
        

#     Miles = float(miles)#convert miles to Miles
#     gallons = int(input("Number of gallons needed:"))#convert gallons to int
#     total_m += Miles#increment
#     total_g += gallons#increment
#     print("Mileage this tank =","{:.1f}".format(Miles/gallons))# formula of finding Mileage
    



# #pi
# #Yuzhe Zheng
# #
# #find difference between estimation and pi 
# Terms = int(input("Number of terms:"))
# #Initialize every values
# error_odd = 0
# error_even = 0
# times = 0
# ans = 0
# odd_times = 0
# even_times = 0
# total_ans = 0
# pos_ans = 0
# neg_ans = 0
# pi = 3.1415926535
# # while times < Terms + 1:
# #     times += 1
# if Terms % 2 == 0: # even case
#     while times <= ((Terms/2) -1):
#         pos_ans += 4/ ( (4 * times) +1 )# we only need n = 0,1,2 if input = 6 for positive terms
#         times += 1#increment set here, to let times start at 0
#     times = 0 #reset time to 0, to prevent the next while loop start from ((Terms/2) -1)
#     while times < (Terms/2):
#         times += 1#increment set here, to let times start at 1
#         neg_ans -= 4/ ( 4 * (times) -1 )# we only need n = 1,2,3 if input = 6 for negative terms
#     total_ans = pos_ans + neg_ans
#     error_even = pi - total_ans#find difference b.w. the real pi and estimation, when input is a even number
#     print("Estimate of pi: ",total_ans)
#     print("Error: ","{:.9f}".format(error_even))

# if Terms % 2 == 1: #ODD case
#     while times <= (((Terms +1 )/2))-1:
#         pos_ans += 4/ ( (4 * times) +1 )# we only need n = 0,1,... 499 if inputs = 999  for positive terms
#         times += 1#increment set here, to let times start at 0
#     times = 0#reset time to 0, to prevent the next while loop start from (((Terms +1 )/2))-1
#     while times < (((Terms +1 )/2)-1):# count from 
#         times += 1#increment set here, to let times start at 1
#         neg_ans -= 4/ ( 4 * (times) -1 )# we only need n = 1,2...500 if inputs = 999 for negative terms
#     total_ans = pos_ans + neg_ans
#     error_odd = pi - total_ans#find difference b.w. the real pi and estimation, when input is a odd number
#     print("Estimate of pi: ",total_ans)
#     print("Error: ","{:.9f}".format(error_odd))

        

# #pocket
# #Yuxhe Zheng
# #
# #change money
# print("Compute your pocket change!")
# Q = int(input("Quarters?"))#get input and convert string to integer
# D = int(input("Dimes?"))#get input and convert string to integer
# N = int(input("Nickels?"))#get input and convert string to integer
# P = int(input("Pennies?"))#get input and convert string to integer
# print("The total is", "{:.2f}".format(Q*0.25+D*0.1+N*0.05+P*0.01))#convert result to 2 decimal places


#roth
#Yuzhe Zheng
#
# #find how long it will take to make deposit double
# deposit = float(input("Enter an initial Roth IRA deposit amount:"))
# rate = float(input("Enter an annual percent rate of return:"))
# print("Value after year 1:", "${:.2f}".format(deposit*rate*0.01+deposit))
# years = 1#initialized the year
# total = (deposit*rate*0.01+deposit)#set the initial deposit is the input number
# while total < 2*deposit:# keep running till double
#     total += rate*0.01*total# rate * initial deposit + initial deposit
#     print("Value after year "+ str(years+1)+": ${:.2f}".format(total)) 
#     years +=1 # count years
# print("It will take",years, "years to double your investment with a "+str("{:.1f}".format(rate))+"% APR.")
#         #print the input rate with one float point
#         #to eliminate the space between rate and % symbol, I convert the rate to a string


a = [] 
while True:
    ans = input("Enter the equation: ")
    if ans == 6:
        a.append(ans)
    else:
        break
    

# n = 0 
# print(len(a))
# while n < len(a):
#     n += 1
#     print(a[n])
    










