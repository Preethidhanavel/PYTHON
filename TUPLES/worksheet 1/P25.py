'''Description: Count the number of tuples where every element is divisible by a given integer K.
This builds filtering skills and strengthens logic construction for data validation.
Input: lst = [(3, 6), (9, 12, 15), (4, 8)], K = 3
Output: 2'''
import ast
t=input("Enter the list of tuple:")
t=ast.literal_eval(t)
k=int(input("Enter the number:"))
c=0
for i in t:
    if all ( n%k==0 for n in i):
        c+=1
print("Output:",c)