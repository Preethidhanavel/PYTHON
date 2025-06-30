'''Description: Print the first and last elements of a tuple using positive and negative indexing.
Learn how to access tuple elements using both forward and backward indexes, which is essential for tuple manipulation.
Input: my_tuple = (10, 20, 30, 40, 50)
Output: 10
50'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
print("First element:",t[0])
print("Last element:",t[-1])