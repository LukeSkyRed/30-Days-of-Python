'''
A quick explanation of the algorithm
The algorithm we're going to use to verify card numbers is called the Luhn algorithm, or Luhn formula. 
This algorithm is actually used in real-life applications to test credit or debit card numbers as well as SIM card serial numbers.
The purpose of the algorithm is to identify potentially mistyped numbers, because it can determine whether or not 
it's possible for a given number to be the number for a valid card.

The way we're going to use the algorithm is as follows:

'''

#1 - Remove the rightmost digit from the card number. This number is called the checking digit,and it will be excluded from most of our calculations.
#2 - Reverse the order of the remaining digits.
#3 - For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them. If any of the results are greater than 9, 
#    subtract 9 from those numbers.
#4 - Add together all of the results and add the checking digit.
#5 - If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.

print("###### CREDIT CARD VALIDATOR ######\n")

#create a list from user input and remove extra space
credit_card_number = list(input("Insert credit card number: ").strip())
#remove the last digit
check_digit = credit_card_number.pop()
#reverse the string
credit_card_number.reverse()
#print(credit_card_number)

processed_digits = []

for index,num in enumerate(credit_card_number): 
        if index % 2 == 0:
            double_digit = int(num) * 2
            if double_digit > 9:
                double_digit -= 9
            processed_digits.append(double_digit)
        else:
            processed_digits.append(int(num))

#print(processed_digits)

total = int(check_digit)

for digit in processed_digits:
    total = total + digit

print(total)

if total % 10 == 0:
    print("Number card inserted is Valid!")
else:
    print("Number card is not valid!")













