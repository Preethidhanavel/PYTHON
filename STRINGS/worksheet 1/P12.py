'''Find Close Matches for a String in a List
Explanation: Find list entries that are similar to the given word (helpful for typo correction).
Input: Target = "apple", List = ["apply", "apples", "ape", "maple"]
Expected Output: Close matches: ['apply', 'apples']'''
import ast
import difflib
list=input("Enter the list:")
list=ast.literal_eval(list)
t=input("Enter the target:")
l=[]
for i in list:
    if t.startswith(i)or i.startswith(t):
        l.append(i)
print(l)
close_matches = difflib.get_close_matches(t, list,n=3, cutoff=0.8)
print(close_matches)
for i in list:
    if t[:len(i)] == i or i[:len(t)]==t:
        print(i)