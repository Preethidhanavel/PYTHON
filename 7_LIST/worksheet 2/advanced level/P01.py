'''Task: Write a Python function to reverse a list at a specific location.
Sample input: [1, 2, 3, 4, 5, 6], position: 3
Output: [1, 2, 3, 6, 5, 4]'''

def reverse_from_position(lst, position):
    return lst[:position] + lst[position:][::-1]

import ast
l=input("Enter the list of tuples:")
l=ast.literal_eval(l)
position=int(input("Enter the position:"))


result = reverse_from_position(l, position)
print("Modified list:", result)
