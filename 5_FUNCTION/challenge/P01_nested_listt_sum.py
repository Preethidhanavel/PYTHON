''' Write a function deep_sum(lst) that takes a nested list of integers (arbitrary levels of nesting) and 
returns the total sum of all integers.'''
import ast

# Function to recursively sum all integers in a nested list
def deep_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, int):  # If item is integer, add to total
            total += item
        elif isinstance(item, list):  # If item is a list, call function recursively
            total += deep_sum(item) 
    return total

# Read input from user (supports nested list input)
n = input("Enter numbers separated by spaces and nested list: ")

# Convert string input to actual Python list safely
l = ast.literal_eval(n)

# Display the list
print("List:", l)

# Display the total sum of all integers in the list
print(f"The total of list element is {deep_sum(l)}")
