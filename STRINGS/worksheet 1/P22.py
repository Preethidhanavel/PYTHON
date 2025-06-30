'''Sort a List of Strings Alphabetically
Explanation: Arrange the list of strings in lexicographical order.
Input: ["pear", "apple", "banana"]
Expected Output: ['apple', 'banana', 'pear']'''
import ast
s=input("Enter the list of strings:")
l=ast.literal_eval(s)
print(sorted(l,key=lambda x:x.lower()))      