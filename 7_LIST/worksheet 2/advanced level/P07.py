'''Task: Write a Python function to remove duplicates from a list while preserving the original order of the remaining elements.
Sample input: [1, 2, 2, 3, 4, 4, 5, 6, 5]
Output: [1, 2, 3, 4, 5, 6]'''
import ast
l=input("Enter the list1:")
l=ast.literal_eval(l)
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print("Output:",l1)