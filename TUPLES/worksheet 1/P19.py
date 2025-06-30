'''Description: Identify and print elements that occur more than once in a tuple.
Spotting duplicates in sequences is common in data cleaning and interviews.
Input: t = (2, 4, 6, 2, 8, 4, 6, 2)
Output: 2, 4, 6'''
import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)
f={}
for i in t:
    f[i]=t.count(i)
freq=[str(key) for key,value in f.items() if value>1]
print(freq)
print(", ".join(freq))