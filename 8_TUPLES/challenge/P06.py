'''Description: Flatten a tuple that contains lists as elements into a single tuple containing all the items.
This helps in unifying data structures for easier processing and analysis.
Input: t = ([1, 2], [3, 4], [5, 6])
Output: (1, 2, 3, 4, 5, 6)'''
import ast
t=input("Enter the  tuple of list:")
t=ast.literal_eval(t)
l=[]
for i in t:
    l.extend(i)

print(tuple(l))