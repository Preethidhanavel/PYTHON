'''Task: Write a Python program to flatten a shallow list.
Sample input: [[1, 2], [3, 4], [5, 6]]
Output: [1, 2, 3, 4, 5, 6]'''

import ast
l=input("Enter the nested list:")
l=ast.literal_eval(l)
l1=[]
for i in l:
    if type(i)==list:
        l1.extend(i)
    else:
        l1.append(i)
print("After flattening:",l1)