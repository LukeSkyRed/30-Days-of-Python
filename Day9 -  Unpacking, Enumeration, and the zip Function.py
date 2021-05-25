#Unpacking, Enumeration, and the zip Function

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

'''

For each iteration of the loop, movies gives us a single tuple. 
Python sees that the tuple has three values in it, and we've defined three names. 
It therefore takes the first item in the tuple and assigns it to the name title; 
it takes the second item and assigns it to director; and it takes the third value and assigns it to year

'''

for title, director, year in movies:
	print(f"{title} ({year}), by {director}")

#Using ENUMERATE to print the enumerate the elements of the list
for counter, (title, director, year) in enumerate(movies, start = 1):
	print(f"{counter}. {title} ({year}), by {director}")

#---------------------------------------------------------------------------------------


#1) Below is some simple data about characters from BoJack Horseman:
#The data contains the character name, the voice actor or actress who plays them, and the species of the character.
#Write a for loop that uses destructuring so that you can print each tuple in the following format:
#BoJack Horseman is a horse voiced by Will Arnet.

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for character_name,actor,specie in main_characters:
	print(f"{character_name} is a {specie.lower()} voiced by {actor}")

#---------------------------------------------------------------------------------------

#2)Unpack the following tuple into 4 variables:

("John Smith", 11743, ("Computer Science", "Mathematics"))

#The data represents a student's name, their student id number, and their major and minor disciplines in that order.

name,id_number,(first_discipline,second_disciplice) = ("John Smith", 11743, ("Computer Science", "Mathematics"))

print(f"Student Name: {name}")
print(f"Id Number: {id_number}")
print(f"First discipline: {first_discipline}")
print(f"Second discipline: {second_disciplice}")

#---------------------------------------------------------------------------------------

#3)Investigate what happens when you try to zip two iterables of different lengths. 
#For example, try to zip a list containing three items, and a tuples containing four items.

name = ["Luca","Marco","Irene"]
age = (45,65,68,87)

item_list = list(zip(name,age))

print(item_list)

#[('Luca', 45), ('Marco', 65), ('Irene', 68)]
'''
ZIP stopped once we reached the end of the shortest collection. 
If we have three collections of different lengths, the same thing will happen.
This is a really important detail to keep in mind, because it can lead to accidental data loss if you're not careful.

'''

