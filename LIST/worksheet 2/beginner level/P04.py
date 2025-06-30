'''Task: Write a Python program to get the smallest number from a list.
Sample input: [1, 2, 3, 4, 5]
Output: 1'''
import ast
l=input("Enter the lsit:")
l=ast.literal_eval(l)
minimum=l[0]
for  i in range(1,len(l)):
    if minimum>l[i]:
        minimum=l[i]
print(f"Output:{minimum}")
print(min(l))