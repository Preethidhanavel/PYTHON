'''Description: Iterate through all elements in a tuple and print each one on a separate line.
Looping over tuples is a fundamental skill for data processing and display.
Input: t = ("apple", "banana", "cherry")
Output: apple
banana
cherry'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
for i in t:
    print(i)