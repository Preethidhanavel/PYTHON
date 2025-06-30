'''Description: Count how many times a particular value occurs in a tuple.
Element frequency counting is useful for analytics and validation tasks.
Input: t = (1, 2, 3, 2, 2, 4), Count: 2
Output: 3'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
n=int(input("enter the element to find its frequency in tuple:"))
print("Output:",t.count(n))