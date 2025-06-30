'''Convert a List or Tuple of Characters to a String
Explanation: Combine list/tuple elements into a single string.
Input: ['p', 'y', 't', 'h', 'o', 'n']
Expected Output: "python"'''
import ast
s=input("Enter list or tuple:")
s1=ast.literal_eval(s)
r=''
for i in s1:
    r+=i
print("Output:",r)