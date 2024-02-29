running_count = 0
running_sum = 0
running_min = None #emphasis the data is empty
running_max = None

while True:
    ans = input("Enter a number or 'done'")

    if ans == 'done':
        break

    num = float(ans)
    #update the statistic
    running_count = running_count +1

    running_sum = running_sum + num

    if running_min == None or num < running_min:
        running_min = num

    if running_max == None or num > running_max:
        running_max = num


print(running_count)
print(running_sum)
print(running_min)
print(running_max)

