'''Description: Remove a specific element from a tuple by converting it to a list and back.
Removing elements from tuples is a common interview question testing immutability handling.
Input: t = (1, 2, 3, 4), Remove: 2
Output: (1, 3, 4)'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
t=list(t)
n=int(input("Enter the element to remove:"))
t.remove(n)
print("After adding the tuple is:",tuple(t))