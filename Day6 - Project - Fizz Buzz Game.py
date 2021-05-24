#Day 6 Project: Fizz Buzz

#Fizz Buzz Game
#Rules:
#One player starts by saying the number 1.
#Each player then takes it in turns to say the next number, counting one at a time.
#If the number is divisible by 3, instead of saying the number, the player should say, "Fizz".
#If the number is divisible by 5, instead of saying the number, the player should say, "Buzz".
#If the number is divisible by 3and5, instead of saying the number, the player should say, "Fizz Buzz".
#If you make a mistake, you're usually eliminated from the game, and the game continues until there's only a single player remaining.

limit = int(input("Enter range: "))

for num in range(1,limit):
    #alternative with single check
    if (num % 15 == 0):
    #if (num % 3 == 0) and (num % 5 == 0):
        print("Fizz Buzz")
    elif(num % 3 == 0):
        print("Fizz")
    elif(num % 5 == 0):
        print("Buzz")
    else:
        print(num)




