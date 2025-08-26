'''Description: Remove all empty tuples from a list of tuples and print the cleaned list.
This is useful for sanitizing input data before processing.
Input: lst = [(), (), ('a', 'b'), ('c',)]
Output: [('a', 'b'), ('c',)]'''
import ast
t=input("Enter the list of tuple with empty tuple also:")
t=ast.literal_eval(t)

l=[]
for i in t:
    if len(i)>=1:
        l.append(i)
print("After removing empty tuple:",l)