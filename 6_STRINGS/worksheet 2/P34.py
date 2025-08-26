'''Replace Multiple Words at Once
Explanation: Simultaneously replace several different words in a string with new ones.
Input: String = "I like apples and bananas.", Replace: {"apples": "oranges", "bananas": "grapes"}
Expected Output: "I like oranges and grapes."'''
import ast
s=input("Enter the string:")
d=input("Enter the dict for replacement:")
d=ast.literal_eval(d)

s=s.split()
print(s)
res=''
for i in s:
    if i in d:
        w=d.get(i)
        res+=' '+w
    else:
        res=res+' '+i

print(res)