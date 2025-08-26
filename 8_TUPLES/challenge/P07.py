'''Description: Convert a nested tuple (tuple of tuples) into a dictionary with custom keys for each inner tuple.
Such conversion is useful for representing structured data with key-value mappings for clarity and access.
Input: t = (('x', 1), ('y', 2), ('z', 3))
Output: {'x': 1, 'y': 2, 'z': 3}'''
import ast
t=input("Enter the  nested tuple:")
t=ast.literal_eval(t)
f={}
for n in t:
    f[n[0]]=n[1]
print(f)
print(dict(t))
