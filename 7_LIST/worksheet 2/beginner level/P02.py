'''Task: Write a Python program to multiply all the items in a list.
Sample input: [1, 2, 3, 4]
Output: 24'''
import ast
import math
l=input("Enter the listt:")
l=ast.literal_eval(l)
pdt=1
for i in l:
    pdt*=i
print(f"Outpur:{pdt}")
print(math.prod(l,start=1))