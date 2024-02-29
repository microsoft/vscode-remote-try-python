# #read_temp_file.py
# #Yuzhe Zheng
# #
# #read and print file
# file = input("Temperature anomaly filename:")
# infile = open(file,"r")# open file in read mode

# for line in infile: #go though each element in the file
#     line = line.replace(","," ")# replace common to an empty space
#     line = line.strip()# fet rid off the gap between two line
#     print(line)
    
# #temp_file_stats.py
# #Yuzhe Zheng
# #
# #find the max and min temp and the year corresponded
# file  = input ("Temperature anomaly filename:")
# infile = open(file,"r")# open file in read mode

# list_num = []#create empty list for temp
# list_year = []#create empty list for year
# for line in infile:
#     try:# use try to eliminate ValueError
#         num = float(line[5:len(line)-1])# temp in the table
#         list_num.append(num)#put the temp to the list

#         year = int(line[0:4])# temp in the table
#         list_year.append(year)#put the year to the list
#     except:
#         continue#skip the first row

# #the one temp correspond to one year, so they share same index
# # use for loop to find where the max temp in the list
# n = 0
# for i in list_num:
#     n += 1# increment
#     if i == max(list_num):
#         break

# # use for loop to find where the min temp in the list
# m = 0
# for i in list_num:
#     m += 1# increment
#     if i == min(list_num):
#         break
        
# print("Min temp:",list_num[m-1],"in",list_year[m-1])
# print("Max temp:",list_num[n-1],"in",list_year[n-1])


# #temp_list.py
# #Yuzhe Zheng
# #
# #
# file  = input ("Temperature anomaly filename:")
# infile = open(file,"r")# open file in read mode
# list = []# create a empty list for storing temp
# for line in infile:#go through every line in file
#     try:#use try to eliminate ValueError
#         temp = float(line[5:len(line)-1]) #convert temp to float
#         list.append(temp)# append every temp to the list

#     except:
#         continue#skip first line
# print(list)

# #first_ave.py 
# #Yuzhe Zheng
# #
# # find the average of the tempure within the given period of time
# file  = input ("Temperature anomaly filename:")
# infile = open(file,"r")# open file in read mode
# list = []# create a empty list for storing temp
# for line in infile:#go through every line in file
#     try:#use try to eliminate ValueError
#         temp = float(line[5:len(line)-1]) #convert temp to float
#         list.append(temp)# append every temp to the list

#     except:
#         continue#skip first line
# k = int(input("Enter window size:"))
# index = k # number of year
# year = 1880 + index # domain of year
# ave = sum(list[index-k:index+k+1]) / (2*k+1) # sum up the temp in the time period 1800 to 1800 + index and divid by k +1 year
# print(str(year)+str(",{:.4f}".format(ave))) # concatenate two string. First, set up the 4 float limitation then, concatenate two string together

        

# #moving_ave.py 
# #Yuzhe Zheng
# #
# # find the average of the tempure within the given period of time
# file  = input ("Temperature anomaly filename:")
# infile = open(file,"r")# open file in read mode
# list = []# create a empty list for storing temp
# for line in infile:#go through every line in file
#     try:#use try to eliminate ValueError
#         temp = float(line[5:len(line)-1]) #convert temp to float
#         list.append(temp)# append every temp to the list

#     except:
#         continue#skip first line

# k = int(input("Enter window size:"))
# temp = []#empty list for avg temp
# years = []#empty list for year
# for i in range(k, len(list)- k):
#     year = 1880 + i # domain of year
#     ave = sum(list[i-k:i+k+1]) / (2*k+1) # sum up the temp in the time period 1800 to 1800 + index and divid by k +1 year
#     temp.append(ave)#store average temp in to the list
#     years.append(year)#store year to the list

# i = 0 #initialize the increment value
# while i < len(temp):#use for loop print out every value in the temp years and temp list
#     i += 1#increment
#     print(str(years[i-1])+str(",{:.4f}".format(temp[i-1])))# concatenate two string. First, set up the 4 float limitation then, concatenate two string together


# #moving_ave_csv.py
# #Yuzhe Zheng
# #
# # 
file  = input ("Temperature anomaly filename:")
infile = open(file,"r")# open file in read mode
list = []# create a empty list for storing temp
for line in infile:#go through every line in file
    try:#use try to eliminate ValueError
        temp = float(line[5:len(line)-1]) #convert temp to float
        list.append(temp)# append every temp to the list

    except:
        continue#skip first line

k = int(input("Enter window size:"))
outfile = input("Out file name: ")# ask for output file name
temp = []#empty list for avg temp
years = []#empty list for year
for i in range(k, len(list)- k):
    year = 1880 + i # domain of year
    ave = sum(list[i-k:i+k+1]) / (2*k+1) # sum up the temp in the time period 1800 to 1800 + index and divid by k +1 year
    temp.append(ave)#store average temp in to the list
    years.append(year)#store year to the list

result = open(outfile,"w")#open output file in write mode
result.write("Year,Value\n")#print the first line in the output file
i = 0 #initialize the increment value

while i < len(temp):#use for loop print out every value in the temp years and temp list
    i += 1#increment
    result.write(str(years[i-1])+str("{:.4f}\n".format(temp[i-1]))) # concatenate two string. First, set up the 4 float limitation then, concatenate two string together
    # move each line from two lists to outfile



   






