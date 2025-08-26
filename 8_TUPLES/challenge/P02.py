'''Description: Remove duplicate tuples from a list of tuples and print the unique tuples only.
This is important for ensuring data integrity and is frequently used in database and data analysis tasks.
Input: lst = [(1, 2), (3, 4), (1, 2), (5, 6)]
Output: [(1, 2), (3, 4), (5, 6)]'''
import ast
t=input("Enter the list of tuple:")
t=ast.literal_eval(t)
l=[]
for i in t:
    if i not in l:
        l.append(i)

print(l)