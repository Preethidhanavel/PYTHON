'''Task: Write a Python program to create a list of squares from 1 to 10 using list comprehension.
Sample input: Range: 1 to 10
Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'''
import ast
l=input("Enter the nested list:")
l=ast.literal_eval(l)
print([i**2 for i in l])