'''Task: Write a Python program to s all the items in a list.
Sample input: [1, 2, 3, 4, 5]
Output: 15'''
import ast
l=input("Enter the lsit:")
l=ast.literal_eval(l)
s=0
for i in l:
    s+=i
print(f"Outpur:{s}")
print(f"{sum(i for i in l)}")
print(sum(l))