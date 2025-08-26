'''Description: Remove tuples from a list where every element is None, keeping only valid data tuples.
This is a real-world data cleaning task commonly required when working with incomplete or missing data.
Input: lst = [(None, None), (1, 2), (None, 3), (4, 5), (None, None)]
Output: [(1, 2), (None, 3), (4, 5)]'''

import ast
t=input("Enter the  list of tuple:")
t=ast.literal_eval(t)
l=[]
for i in t:
    if any(n for n in i):
        l.append(i)
print(l)