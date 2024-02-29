#car
#Yuzhe Zheng
#
#guess the price of car
print("Guess the price and win the prize!")
n = 0# initialized the value
while True:
    n += 1# increment
    price = int(input("Enter your guess:"))
    if price == 44500 and n <= 5:# take 5 times and guess correctly, win
        print("It took",n, "guesses.")
        print("You won the car!")
        break
    if price == 44500 and n > 5:# although got correct answer, but still lose
        print("It took",n, "guesses.")
        print("Too many guesses!")
        break

    if price > 44500:# to see if the answer is too high or too low
        print("Too high!")
    if price < 44500:
        print("Too low!")