'''Task: Write a Python program to remove duplicates from a list.
Sample input: [1, 2, 3, 2, 4, 3, 5]
Output: [1, 2, 3, 4, 5]'''

import ast
l=input("Enter the list:")
l=ast.literal_eval(l)
res=[]
for i in l:
    if i not in res:
        res.append(i)
print(res)
print(list(set(l)))