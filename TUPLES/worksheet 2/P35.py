'''Description: Find all possible pair combinations from two tuples, combining each element from the 
first tuple with each from the second.
This problem introduces the concept of Cartesian product and is useful for combinatorial tasks.
Input: t1 = (1, 2), t2 = (3, 4)
Output: [(1, 3), (1, 4), (2, 3), (2, 4)]'''
import ast
t1=input("Enter the tuple 1:")
t1=ast.literal_eval(t1)
t2=input("Enter the tuple 2:")
t2=ast.literal_eval(t2)
l1=[]
for i in t1:
    l=[i]
    for j in t2:
        l.append(j)
        l1.append(tuple(l))
        l=[i]
print(l1)