'''Description: Find all unique elements present in a tuple of tuples using set logic.
This teaches set operations and how to process nested iterable structures.
Input: t = ((1, 2), (2, 3), (4, 5))
Output: {1, 2, 3, 4, 5}'''
import ast
t=input("Enter the nested tuple:")
t=ast.literal_eval(t)
l=[]
for i in t:
    l.extend(list(i))

print("Output:",set(l))