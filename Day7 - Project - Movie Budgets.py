
'''
#Below you'll find a list which contains the relevant data about a selection of movies.
#Each item in the list is a tuple containing a movie name and movie budget in that order:
'''

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

'''
#For this project, your program should do the following:

#1 - Calculate the average budget of all movies in the data set.
#2 - Print out every movie that has a budget higher than the average you calculated.
#You should also print out how much higher than the average the movie's budget was.
#3 - Print out how many movies spent more than the average you calculated.

#If you want a little extra challenge, allow users to add more movies to the data set before running the calculations.

'''

#ask the user how many movies he wnat to add
new_movies_count = int(input("How many movies do you want to add? "))

for count in range(new_movies_count):
    name = input("Movie title: ")
    budget = int(input("Movie Budget: "))
    new_movie = (name,budget)
    movies.append(new_movie)


#calculate the average budget
total_budget = 0

for movie in movies:
    total_budget = total_budget + movie[1]    

average_budget = int(total_budget / len(movies))

print(f"The budget average of all movies is €{average_budget}")


#calculate how many movies have the budget higher than the average 
over_average_movies=[]

for movie in movies:
    if movie[1] > average_budget:
        over_average_movies.append(movie[0])
        print(f"Movie {movie[0]} has a budget higher than the average of " + str(movie[1] - average_budget))

print(f"{len(over_average_movies)} movies has the budget higher than the average")