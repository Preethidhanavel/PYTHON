'''Sort a List of Strings Alphabetically
Explanation: Arrange the list of strings in lexicographical order.
Input: ["pear", "apple", "banana"]
Expected Output: ['apple', 'banana', 'pear']'''
import ast   # Import ast for safe evaluation of list input

# Take input from user (list of strings in Python format)
s = input("Enter the list of strings: ")

# Convert input string into actual Python list
l = ast.literal_eval(s)

# Sort list of strings in case-insensitive manner (using str.lower)
print(sorted(l, key=lambda x: x.lower()))
    