'''Description: Find the index of a specified value in a tuple using the index() method.
Locating elements within tuples is crucial for data lookup and manipulation.
Input: t = ("cat", "dog", "rabbit"), Find: "dog"
Output: 1'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
n=input("enter string to find its position:")
print("Output:" ,t.index(n))