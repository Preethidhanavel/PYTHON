'''Description: From a list of tuples, keep only those where all numbers are positive.
Filtering based on condition is commonly used for cleaning or selecting data.
Input: lst = [(1, 2), (-3, 4), (5, 6)]
Output: [(1, 2), (5, 6)]'''
import ast
t=input("Enter the list of tuple:")
t=ast.literal_eval(t)

l=[]
for i in t:
    if all ( n>=0 for n in i):
        l.append(i)
print(l)