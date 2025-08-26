'''Description: Given a list of tuples, count and print the number of elements before encountering a tuple in the list.
This teaches control flow and type checking within mixed-type data collections.
Input: lst = [1, 2, 3, (4, 5), 6]
Output: 3'''

import ast
t=input("Enter the  list of tuple:")
t=ast.literal_eval(t)
s=0
for i in t:
    if type(i)==tuple:
        break
    s+=1
print("The sum is:",s)