#Day 4: Basic Python Collections

#Create a movies list containing a single tuple.
# The tuple should contain:
# a movie title, 
# the director’s name, 
# the release year of the movie,
# and the movie’s budget.
movies_list  = [("Gladiator","Ridle Scott","2000","$100,000,000")]

#Use the input function to gather information about another movie. 
#You need a title, director’s name, release year, and budget.
title = input("Enter movie title: ")
director = input("Enter movies director: ")
year = input("Enter release year: ")
budget = input("Enter movie budget ")

#Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote 
#in the movies list.
new_movie = (title,director,year,budget)

#Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f"Movie Title: {new_movie[0]}, Release year: {new_movie[2]}")

#Add the new movie tuple to the movies collection using append.
movies_list.append(new_movie)

#Print both movies in the movies collection.
print(movies_list[0])
print(movies_list[1])

#Print ONLY the movies title
print(f"First Movies Title: {movies_list[0][0]}, Second Movie Title: {movies_list[1][0]}")

#Remove the first movie from movies. Use any method you like.
movies_list.pop(0)

print(movies_list)
