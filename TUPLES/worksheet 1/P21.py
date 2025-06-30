'''Description: Sort a list of (name, age) tuples by the second element (age) in ascending order.
Sorting tuples by a specific key is frequently used for ordering structured data.
Input: lst = [("Alice", 25), ("Bob", 20), ("Eve", 22)]
Output: [('Bob', 20), ('Eve', 22), ('Alice', 25)]'''

import ast
t=input("Enter the list of tuple:")
t=ast.literal_eval(t)

print(sorted(t,key=lambda x:x[-1]))