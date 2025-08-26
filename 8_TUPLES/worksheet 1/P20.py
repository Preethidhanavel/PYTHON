'''Description: Check whether all elements in a tuple are unique using set comparison.
Ensures data integrity in scenarios where duplicate values are not allowed.
Input: t = (1, 2, 3, 4, 5)
Output: True'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
s=set(t)
if len(t)==len(s):
    print("True")
else:
    print("False")