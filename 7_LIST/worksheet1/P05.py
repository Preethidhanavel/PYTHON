''' Sorting and Copying Lists
Log Session a list of numbers: [3, 1, 4, 2, 5].
Sort the list in ascending order.
Sort the list in descending order.
Copy the sorted list to a new list.
Print both lists to verify they are separate copies.'''

l=[3,1,4,2,5]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
n=l.copy()
n[2]=6
print("After modifying new list:")
print('newlist',n)

print('sortedlist',l)