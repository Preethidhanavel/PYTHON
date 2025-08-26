'''List Methods Practice
Log Session a list: colors = ["red", "green", "blue", "green"].
Use the count() method to find how many times "green" appears.
Use the index() method to find the position of "blue".
Reverse the list using the reverse() method.
Clear the list using the clear() method.'''

# Initial list
colors = ["red", "green", "blue", "green"]
print("Original list:", colors)

#  count() 
green_count = colors.count("green")
print("Count of 'green':", green_count)

# index() 
blue_index = colors.index("blue")
print("Index of 'blue':", blue_index)

# reverse()
colors.reverse()
print("List after reversing:", colors)

# clear()
colors.clear()
print("List after clearing:", colors)
