'''Task: Write a Python program to insert an element at a specified position in a list.
Sample input: [1, 2, 3, 4], element: 5, position: 2
Output: [1, 2, 5, 3, 4]'''
import ast
l=input("Enter the nested list:")
l=ast.literal_eval(l)
ele=int(input("Enter the element :"))
pos=int(input("Enter the position:"))
l.insert(pos,ele)
print(l)