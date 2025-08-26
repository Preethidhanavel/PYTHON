'''Task: Write a Python program to find the common elements between two lists.
Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: [3, 4]'''
import ast
l=input("Enter the list1:")
l=ast.literal_eval(l)
l1=input("Enter the list2:")
l1=ast.literal_eval(l1)
res=[]
for i in l:
    if i in l1:
        if i not in res:
            res.append(i)
print("Output:",res)