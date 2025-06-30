'''Description: Convert a tuple of nested tuples into a single flat tuple.
Flattening data structures is often needed for uniform data processing and analysis.
Input: t = ((1, 2), (3, 4), (5, 6))
Output: (1, 2, 3, 4, 5, 6)'''
import ast
t=input("Enter the nested tuple:")
t=ast.literal_eval(t)
l=[]
for i in t:
    l.extend(list(i))
print(tuple(l))