'''Description: Reverse the order of items in a tuple and print the result.
This practice is helpful in problems requiring reverse traversal or reordering.
Input: t = (10, 20, 30, 40)
Output: (40, 30, 20, 10)'''
import ast
def reverse_tuple(t):
    return t[::-1]
t=input("Enter the tuple:")
t=ast.literal_eval(t)
print("after reversing:",reverse_tuple(t))