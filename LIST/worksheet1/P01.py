'''List Creation and Indexing
Log Session a list named fruits containing "apple", "banana", and "cherry".
Print the second item in the list.
Change the value from "banana" to "kiwi".
Print the updated list.
Determine the length of the list.'''
import ast
# Create the list
fruits =input("Enter the list:")
fruits=ast.literal_eval(fruits)

# Print the second item (index 1)
print("Second item:", fruits[1])

# Change "banana" to "kiwi"
for i in range(len(fruits)):
    if fruits[i] == "banana":
        fruits[i]='kiwi'

# Print the updated list
print("Updated list:", fruits)

#Print the length of the list
print("Length of the list:", len(fruits))
