'''Looping Through Lists
Log Session a list of numbers from 1 to 5.
Use a for loop to print each number.
Use a while loop to print each number.
Use list comprehension to create a new list with each number squared.'''

import ast
l=input("Enter the list having numbers from 1 to 5:")
l=ast.literal_eval(l)
for i in l:
    print(i,end='')
i=0
while i<len(l):
    print(l[i])
    i+=1

print([i**2 for i in l])