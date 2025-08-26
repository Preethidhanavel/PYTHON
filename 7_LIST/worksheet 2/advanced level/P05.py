'''Task: Write a Python function to check if a given list is a palindrome (reads the same forwards and backwards).
Sample input: [1, 2, 3, 2, 1]
Output: True'''
import ast
def check_pallindrome(l):
    i=0
    j=len(l)-1
    while(i<j):
        if l[i]!=l[j]:
            return False
        i+=1
        j-=1
    return True
l=input("Enter the list :")
l=ast.literal_eval(l)
if check_pallindrome(l):
    print(True)
else:
    print(False)