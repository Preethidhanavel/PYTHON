'''Task: Write a Python program to unzip a list of tuples into individual lists.
Sample input: [(1, 'a'), (2, 'b'), (3, 'c')]
Output: [1, 2, 3], ['a', 'b', 'c']'''
import ast
l=input("Enter the list of tuples:")
l=ast.literal_eval(l)
a, b = zip(*l)

# Convert the results to lists
a = list(a)
b = list(b)

print(a)
print(b)
a1=[x[0]for x in l]
b1=[x[1] for x in l]
print(a1,'\n',b1)