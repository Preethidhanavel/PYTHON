'''Description: Add an item to a tuple by converting it to a list and back to a tuple.
This demonstrates tuple immutability and how to work around it for adding elements.
Input: t = (1, 2, 3), Add: 4
Output: (1, 2, 3, 4)'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
t=list(t)
n=int(input("Enter the element to add:"))
t.append(n)
print("After adding the tuple is:",tuple(t))