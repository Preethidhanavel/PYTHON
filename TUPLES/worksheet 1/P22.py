'''Description: Sort a list of tuples by the total number of digits across all elements in each tuple.
This requires counting the digits and sorting accordingly, which strengthens comprehension of tuple processing.
Input: lst = [(1, 2), (10, 11), (3, 44)]
Output: [(1, 2), (3, 44), (10, 11)]'''
import ast
def length(s1):
    return sum([len(str(i)) for i in s1])
t=input("Enter the list of tuple:")
t=ast.literal_eval(t)

s=sorted(t,key=length)
print(s)