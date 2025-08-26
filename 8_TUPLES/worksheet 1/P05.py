'''Description: Slice a tuple to obtain a sub-tuple containing elements from index 1 to 3.
Slicing is important for extracting parts of a tuple without modifying the original.
Input: t = (0, 1, 2, 3, 4, 5)
Output: (1, 2, 3)'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
print("After slicing:",t[1:4])