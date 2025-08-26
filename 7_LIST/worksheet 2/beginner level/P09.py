'''Task: Write a Python program to clone or copy a list.
Sample input: [1, 2, 3, 4]
Output: [1, 2, 3, 4]'''
import ast
l=input("Enter the list:")
l=ast.literal_eval(l)
l1=l.copy()
print("after copy:",l1)