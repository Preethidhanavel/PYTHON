'''Task: Write a Python function to find the union and intersection of two lists.
Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: Union: [1, 2, 3, 4, 5, 6]
Intersection: [3, 4]'''
import ast
l=input("Enter the list1:")
l=ast.literal_eval(l)
l1=input("Enter the list2:")
l1=ast.literal_eval(l1)
inter=[]

for i in l:
    if i in l1:
        if i not in inter:
            inter.append(i)
u=list(set(l+l1))
print("union:",u,"intersection:",inter)