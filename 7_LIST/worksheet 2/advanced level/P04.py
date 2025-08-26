'''Task: Write a Python function to find the k-th smallest element in a list.
Sample input: [7, 10, 4, 3, 20, 15], k = 3
Output: 7'''
import ast
l=input("Enter the list :")
l=ast.literal_eval(l)
l.sort()
k=int(input("Enter the k-th value:"))
print(l[k-1])