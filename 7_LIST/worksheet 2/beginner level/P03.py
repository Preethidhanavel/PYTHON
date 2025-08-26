'''Task: Write a Python program to get the largest number from a list.
Sample input: [1, 2, 3, 4, 5]
Output: 5'''
import ast
l=input("Enter the lsit:")
l=ast.literal_eval(l)
maximum=l[0]
for  i in range(1,len(l)):
    if maximum<l[i]:
        maximum=l[i]
print(f"Output:{maximum}")
print(max(l))