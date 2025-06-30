'''Description: Compute the frequency of each element in a tuple and return the result as a dictionary.
Element frequency counting is widely used for data summarization, analytics, and validation tasks.
Input: t = (1, 2, 2, 3, 3, 3)
Output: {1: 1, 2: 2, 3: 3}'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
d={}
for i in t:
    d[i]=t.count(i)
print("Output:",d)