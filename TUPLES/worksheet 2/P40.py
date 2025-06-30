'''Description: Perform elementwise AND and XOR operations between two tuples of integers of equal length.
Elementwise bitwise operations are crucial in low-level data processing and algorithm optimization.
Input: t1 = (1, 2, 3), t2 = (2, 2, 2)
Output: AND: (0, 2, 2), XOR: (3, 0, 1)'''

import ast
t1=input("Enter the tuple 1:")
t1=ast.literal_eval(t1)
t2=input("Enter the tuple 2:")
t2=ast.literal_eval(t2)
if len(t1)!=len(t2):
    print("length mismatch")
else:
    a=[]
    x=[]
    for i in range(0,len(t1)):
        a.append(t1[i] & t2[i])
        x.append(t1[i]^t2[i])
    print("AND:",a)
    print("XOR:",x)