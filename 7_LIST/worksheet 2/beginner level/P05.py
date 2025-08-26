'''Task: Write a Python program to count the number of strings where the string length is 2 or more 
and the first and last character are the same from a given list of strings.
Sample input: ['abc', 'xyz', 'aba', '1221']
Output: 2'''
import ast
l=input("Enter the lsit:")
l=ast.literal_eval(l)
c=0
for i in l:
    if len(i)>=2:
        if i[0]==i[len(i)-1]:
            c+=1
print("Count:",c)
       

