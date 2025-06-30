'''Description: Filter a list of tuples, keeping only those where the tuple length or value at a specific index meets a condition.
This task helps develop conditional filtering skills and deeper data selection logic in nested structures.
Input: lst = [(1, 2, 3), (4, 5), (6, 7, 8)], Keep tuples of length 3
Output: [(1, 2, 3), (6, 7, 8)]'''
import ast
t=input("Enter the list of tuples:")
t=ast.literal_eval(t)
n=int(input("Enter 0:length 1:value to keep that tuple alone"))
if n==0:
    l=[]
    le=int(input("Enter the length:"))
    for i in t:
        if len(i)==le:
            l.append(i)
    print(l)
if n==1:
    ind=int(input("Enter the index:"))
    l=[]
    for i in t:
        if i[ind]>3:
            l.append(i)
    print(l)