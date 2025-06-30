'''Description: Check if a specified value exists in a tuple and print the result.
Use the "in" keyword to efficiently search for elements inside a tuple.
Input: my_tuple = ('a', 'b', 'c'), Check: 'b'
Output: True'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
n=input("Enter the element to search:")
if n in t:
    print(True)
else:
    print(False)