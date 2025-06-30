'''Description: Convert a tuple of key-value pairs into a dictionary.
This conversion is fundamental in Python for transitioning between sequence and mapping data types for fast lookups.
Input: t = (('a', 1), ('b', 2), ('c', 3))
Output: {'a': 1, 'b': 2, 'c': 3}'''
import ast
t=input("Enter the nested tuples:")
t=ast.literal_eval(t)
d={}
for i in t:
        d[i[0]]=i[1]
print(d)
print(dict(t))

