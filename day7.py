#Day 7: split, join, and Slices

user_numbers = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
numbers_list = user_numbers.split(",")

print(type(numbers_list))
print(user_numbers)
print(numbers_list) # ['1', '2', '3', '4', '5']


#----------------------------------------------------------------------------------------------------------

#1)Ask the user to enter their given name and surname in response to a single prompt. 
# Use split to extract the names, and then assign each name to a different variable. 
# For this exercise, you can assume that the user has a single given name and a single surname.

complete_name = input("Please enter your complete name: ")
complete_name = complete_name.split()

name = complete_name[0]
surname = complete_name[1]

print(name)
print(surname)

#----------------------------------------------------------------------------------------------------------

#2)Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method.
#Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.


my_list = [1, 2, 3, 4, 5]
processed_item = []

print(my_list)

#processed list, converting number to string, from [1, 2, 3, 4, 5] to ['1', '2', '3', '4', '5']
for item in my_list:
    processed_item.append(str(item))

print(processed_item)
#join method return a string by joining all elements separated by a string separator, in this case " |" 
print(" | ".join(processed_item))

#----------------------------------------------------------------------------------------------------------

#3) Below you’ll find a short list of quotes:

quotes = [
 	"'What a waste my life would be without all the beautiful mistakes I've made.'",
 	"'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
 	"'The very essence of romance is uncertainty.'",
 	"'We are not here to do what has already been done.'"
 ]

#Each quote is a string, but each string actually contains quote characters at the start and end.
#Using slicing, extract the text from each string, without these extra quote marks, and print each quote.
#You may also want to try a solution using strip.

for quote in quotes:
	#print(quote[1:-1])
	print(quote.strip("'"))

#----------------------------------------------------------------------------------------------------------

#4)Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace in the user’s input,
#so you’re going to have to process the string before you find its length.

#remove extra space with strip() function
word = input("Enter a word: ").strip()
#use len to get the lenght of the word
print(f"Lenght of the {word} is " + str(len(word)))

#If you want to take this a little bit further, you an ask the user for a long piece of text.
#You can then tell them how many characters are in the text overall, and you can also provide them a word count.

text = input("Enter some words: ").strip()
character_count = len(text)
#divide  the string text a list, and calculate the lenght of the list using len
word_count = len(text.split())
print(f"Character count: {character_count}")
print(f"Word count: {word_count}")


