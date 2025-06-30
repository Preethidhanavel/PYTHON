'''Description: Print the number of elements in a tuple using the len() function.
Knowing the length of tuples is crucial when iterating or validating data.
Input: t = (10, 20, 30, 40)
Output: 4'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
print("Length of tuple:",len(t))