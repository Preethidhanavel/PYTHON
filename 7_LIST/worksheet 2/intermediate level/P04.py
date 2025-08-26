'''Task: Write a Python program to create a list of even numbers from a given list using list comprehension.
Sample input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [2, 4, 6, 8, 10]'''

import ast
l=input("Enter the nested list:")
l=ast.literal_eval(l)
print([i for i in l if i%2==0])