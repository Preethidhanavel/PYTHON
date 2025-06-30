'''Description: Check if a specified value is present in any of the inner tuples in a tuple of tuples.
This teaches how to search through nested tuples, which is useful in multi-dimensional data handling.
Input: t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), Check: 'White'
Output: True'''

import ast
t=input("Enter the nested tuples:")
t=ast.literal_eval(t)
c=input("Enter the value to check if it is present in tuple or not:")
if any(c in i for i in t):
    print("True")
else:
    print("False")