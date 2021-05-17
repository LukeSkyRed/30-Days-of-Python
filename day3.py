#Day 3: Formatting Strings and Processing User Input

# Using the variable below, print "Hello, world!".
greeting = "Hello, World"

#without format() method)
greeting = greeting + "!"
print(greeting)

#with FORMAT method
greeting = "Hello, World"

print("{}!".format(greeting))

#Ask the user for their name, and then greet the user, using their name as part of the greeting.#
#The name should be in title case, and shouldn't be surrounded by any excess white space.

name = input("Whats your Name? ").strip().title()
print("Hello, {}!".format(name))

#Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".

print("I am " + str(29))

#Format and print the information below using string interpolation:
#The output should look like this:
#Joker (2019), directed by Todd Phillips#

title = "Joker"
director = "Todd Phillips"
release_year = 2019

#with format()

print("{} ({}), directed by {}".format(title,release_year,director))

#with f-string

print(f"{title} ({release_year}), directed by {director}")