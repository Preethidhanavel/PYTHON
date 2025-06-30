'''Description: Change the last value in every tuple in a list to a given value.
This shows how to modify immutable data structures by reconstructing them.
Input: lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)], New value: 100
Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]'''

import ast
t=input("Enter the list of tuple:")
t=ast.literal_eval(t)
n=int(input("Enter the new element to be added:"))
l1=[]
for i in t:
    l=list(i)
    l[len(l)-1]=n
    l1.append(tuple(l))
print("Output:",l1)