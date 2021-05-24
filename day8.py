#Day 8: While Loops

#1) Write a short guessing game program using a while loop. 
#The user should be prompted to guess a number between 1 and 100,
#and you should tell them whether their guess was too high or too low after each guess.
#The loop should keeping running until the user guesses the number correctly.

num = 77

while True:
    guess = int(input("Guess the number: "))
    if guess > num:
        print("Number is too high, retrie!")
    elif guess < num:
        print("Number is too low, retrie!")
    else:
        print("Number guessed!")
        break

#2)Use a loop and the continue keyword to print out every character in the string "Python", except the "o".

word = "Python"

for letter in word:
    if letter == 'o':
        continue
    print(letter)


#3)Using one of the examples from earlier—or a solution entirely of your own create a program 
#that prints out every prime number between 1 and 100.

for dividend in range(2,101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        print(f"{dividend} is a prime number")      
          
    
        







