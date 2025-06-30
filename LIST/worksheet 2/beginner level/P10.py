'''Task: Write a Python program to find the list of words that are longer than n from a given list of words.
Sample input: ['hello', 'world', 'python', 'is', 'great'], n = 4
Output: ['hello', 'world', 'python', 'great']'''
import ast
l=input("Enter the lsit:")
l=ast.literal_eval(l)
n=int(input("Enter the n:"))
l1=[]
for i in l:
    if len(i)>=n:
        l1.append(i)
print("Count:",l1)