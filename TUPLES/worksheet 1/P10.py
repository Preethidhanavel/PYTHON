'''Description: Find and print the maximum and minimum values in a tuple of numbers.
This is helpful for statistical analysis and summarizing numeric data in tuples.
Input: t = (11, 3, 55, 21)
Output: 55
3'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
maximum=minimum=t[0]
for i in t:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
print(f"maximum:{maximum}   minimum:{minimum}")
print("Using builtin function:",max(t),min(t))