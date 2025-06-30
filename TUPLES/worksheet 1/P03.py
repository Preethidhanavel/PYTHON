'''Description: Unpack a tuple into three variables and print each variable separately.
This exercise teaches you how tuple unpacking works and is commonly used in data assignment.
Input: t = (1, 2, 3)
Output: 1
2
3'''

import ast
t=input("Enter the tuple contatining three items:")
t=ast.literal_eval(t)
a,b,c=t
print(a)
print(b)
print(c)