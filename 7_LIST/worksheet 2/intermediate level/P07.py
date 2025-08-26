'''Task: Write a Python program to combine two lists into a dictionary.
Sample input: ['a', 'b', 'c'], [1, 2, 3]
Output: {'a': 1, 'b': 2, 'c': 3}'''
import ast
l=input("Enter the list1:")
l=ast.literal_eval(l)
l1=input("Enter the list2:")
l1=ast.literal_eval(l1)
res = dict(zip(l, l1))
print(res)