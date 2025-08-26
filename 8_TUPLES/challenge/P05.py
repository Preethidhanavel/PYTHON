'''Description: Calculate the average of each column in a tuple of tuples and display the result as a list.
This is helpful for column-wise statistics and is frequently seen in spreadsheet-like computations.
Input: t = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Output: [30.5, 34.25, 27.0, 23.25]'''
import ast
t=input("Enter the nested tuple:")
t=ast.literal_eval(t)

l=[sum(i)/len(i) for i in zip(*t)]
print(l)