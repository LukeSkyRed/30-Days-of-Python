#Day 6: For Loops

movies = [
	(
		"Eternal Sunshine of the Spotless Mind",
		"Michel Gondry",
		2004
	),
	(
		"Memento",
		"Christopher Nolan",
		2000
	),
	(
		"Requiem for a Dream",
		"Darren Aronofsky",
		2000
	)
]

for movie in movies:
	  print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

#use of range assigned to a list
print(list(range(10)))

#use range in for loop
for num in range(10):
    print(num)


#Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: 
#their name, the number of hours worked last week, and their hourly rate. Print how much each employee 
#is due to be paid at the end of the week in a nice, readable format.

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

#calculate the weekly wage
for employee in employees:
	total_pay = employee[1] * employee[2]
	print(f"This week {employee[0]} has to be paid €{total_pay:.2f}")


#calculate the average hourly wage

total = 0
count = 0

for employee in employees:
	total +=  employee[2]
	count += 1

average_wage = total / count

#calculate number of list item using len function
#average_wage = total / len(employess)

print(f"Hourly Wage Avarage is {average_wage}")

for employee in employees:
	if employee[2] > average_wage:
		print(f"{employee[0]} earns more than average")




