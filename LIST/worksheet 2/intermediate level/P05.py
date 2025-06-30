'''Task: Write a Python program to remove all occurrences of a specific element from a list.
Sample input: [1, 2, 3, 2, 4, 2, 5], element to remove: 2
Output: [1, 3, 4, 5]'''
import ast
l=input("Enter the nested list:")
l=ast.literal_eval(l)
n=int(input("Enter the elemnt to remove:"))
print([i for i in l if i!=n ])