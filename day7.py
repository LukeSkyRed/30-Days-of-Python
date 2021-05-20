#Day 7: split, join, and Slices
'''
user_numbers = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
numbers_list = user_numbers.split(",")

print(type(numbers_list))
print(user_numbers)
print(numbers_list) # ['1', '2', '3', '4', '5']



#1)Ask the user to enter their given name and surname in response to a single prompt. 
# Use split to extract the names, and then assign each name to a different variable. 
# For this exercise, you can assume that the user has a single given name and a single surname.

complete_name = input("Please enter your complete name: ")
complete_name = complete_name.split()

name = complete_name[0]
surname = complete_name[1]

print(name)
print(surname)
'''
#2)Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method.
#Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.

my_list = [1, 2, 3, 4, 5]
processed_item = []

#processed list, converting number to string, from [1, 2, 3, 4, 5] to ['1', '2', '3', '4', '5']
for item in my_list:
    processed_item.append(str(item))

print(processed_item)
#join method return a string by joining all elements separated by a string separator, in this case |
processed_item = " | ".join(processed_item)
print(" | ".join(processed_item)








