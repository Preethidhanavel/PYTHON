'''Description: Convert a tuple of string numbers to a tuple of integers using comprehension.
This is important for data cleaning and type conversion in real-world datasets.
Input: t = (("11", "22"), ("33", "44"))
Output: ((11, 22), (33, 44))'''
import ast
t=input("Enter the tuple of string numbers:")
t=ast.literal_eval(t)
print(tuple( tuple(int(n) for n in i )for i in t))
