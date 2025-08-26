'''List Comprehension
Log Session a list of fruits: "apple", "banana", "cherry", "kiwi", "mango".
Use list comprehension to create a new list containing fruits with the letter "a".
Convert all fruit names to uppercase using list comprehension.
Replace "banana" with "orange" using list comprehension.'''

import ast
# Create the list
fruits =input("Enter the list:")
fruits=ast.literal_eval(fruits)

print([i for i in fruits  if 'a'in i])
print([i.upper() for i in fruits ])
print( ["orange" if i == "banana" else i for i in fruits])