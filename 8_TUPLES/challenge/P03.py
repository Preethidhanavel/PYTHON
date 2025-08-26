'''Description: Order a list of tuples using an external list that defines the custom order for sorting.
This skill is valuable for implementing custom sorting logic when default Python sorting isn't sufficient.
Input: lst = [('b', 2), ('a', 1), ('c', 3)], order = ['a', 'b', 'c']
Output: [('a', 1), ('b', 2), ('c', 3)]'''
import ast
t=input("Enter the list of tuple:")
t=ast.literal_eval(t)

l=input("Enter the custom order list for sorting:")
res=[]
x=[]
for i in t:
    x.append(i[0])
for i in l:
    if i in x:
        res.append(t[x.index(i)])
print(res)