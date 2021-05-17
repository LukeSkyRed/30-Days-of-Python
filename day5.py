#Day 5: Conditionals and Booleans

#Try to use the is operator or the id function to investigate the difference between this:

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print(numbers is new_numbers)   #false
#check the memory address allocation
print(id(numbers) == id(new_numbers))

#Are new_numbers and numbers the same thing? What about numbers before and after we append 5?

numbers.append(5)
print(id(numbers))

#Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.

number = float(input("enter a number: "))

if number == 0:
    print(f"{number} is 0")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is positive")


#Write a program to determine whether an employee is owed any overtime. 
#You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
#If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, 
#as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours.
#In effect, the employees get paid 110% of their hourly wage for any overtime.

name = input("Enter you name: ")
hour_worked = float(input("How many hour did you work this week? "))
hourly_waged = float(input("Whats your hourly wage? "))

if hour_worked > 40:
    regular_pay = 40 * hourly_waged
    overtime_pay = (hour_worked - 40) * hourly_waged * 1.1
    total_pay = int(regular_pay + overtime_pay)
else:
    total_pay = hour_worked * hourly_waged

print(f"{name} is own {total_pay}€")


