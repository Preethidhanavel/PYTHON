'''Adding and Removing Items
Append "orange" to the fruits list.
Insert "mango" at the second position.
Remove "apple" from the list.
Use the pop() method to remove the last item.
Clear the entire list.'''

import ast
# Create the list
fruits =input("Enter the list:")
fruits=ast.literal_eval(fruits)

# Append "orange" to the list
fruits.append("orange")
print("After appending 'orange':", fruits)

# Insert "mango" at the second position (index 1)
fruits.insert(1, "mango")
print("After inserting 'mango' at index 1:", fruits)

# Remove "apple" from the list
fruits.remove("apple")
print("After removing 'apple':", fruits)

# Use pop() to remove the last item
last_item = fruits.pop()
print("After popping last item ('{}'):".format(last_item), fruits)

# Clear the entire list
fruits.clear()
print("After clearing the list:", fruits)
