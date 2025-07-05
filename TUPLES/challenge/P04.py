'''Description: Given a tuple matrix (tuple of tuples), add elements row-wise and print the result as a list.
This demonstrates processing multi-dimensional tuple data, a common need in scientific and tabular data analysis.
Input: t = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
Output: [6, 15, 24]'''
import ast
t=input("Enter the nested tuple:")
t=ast.literal_eval(t)
print(list(sum(i) for i in t))
