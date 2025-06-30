'''Description: Convert a list to a tuple and a tuple to a list using built-in functions.
Mastering conversion between these types is vital for interoperability in Python programs.
Input: lst = [1, 2, 3], tup = (4, 5, 6)
Output: Tuple: (1, 2, 3)
List: [4, 5, 6]'''
import ast
l=input("Enter the list:")
l=ast.literal_eval(l)
t=input("Enter the tuple:")
t=ast.literal_eval(t)
print(f"After conversion: list to tuple {tuple(l)}",f"tuple to list {list(t)}")