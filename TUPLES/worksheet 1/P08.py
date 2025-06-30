'''Description: Join two tuples together using the + operator and print the result.
Concatenation helps combine multiple tuples into a single sequence for further processing.
Input: t1 = (1, 2), t2 = (3, 4)
Output: (1, 2, 3, 4)'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
t1=input("Enter the tuple:")
t1=ast.literal_eval(t1)
print("After concatenation:",t+t1)