'''Description: Compute the element-wise sum of multiple tuples of equal length.
This exercise teaches how to combine tuples by adding corresponding elements, often used in mathematical and data processing tasks.
Input: t1 = (1, 2, 3, 4), t2 = (3, 5, 2, 1), t3 = (2, 2, 3, 1)
Output: (6, 9, 8, 6)'''
import ast
t1=input("Enter the tuple 1:")
t1=ast.literal_eval(t1)
t2=input("Enter the tuple 2:")
t2=ast.literal_eval(t2)
t3=input("Enter the tuple 3:")
t3=ast.literal_eval(t3)
if not (len(t1) and len(t2) and len(t3)):
    print("length mismatch:")
else:
    l=[]
    for i in range(0,len(t1)):
        s=t1[i]+t2[i]+t3[i]
        l.append(s)
    print("Output:",tuple(l))