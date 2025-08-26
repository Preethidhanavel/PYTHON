#Explain the difference between mutable and immutable data types in Python, with practical examples.
#immutable
a = 10          # a has value 10
b = a           # b also gets value 10
a = a + 5       # a is updated to 15 (10 + 5)
print(a)        # prints 15
print(b)        # prints 10 (b is not changed)

# mutable example
lst1 = [1, 2, 3]     # lst1 is a list
lst2 = lst1          # lst2 points to the same list
lst1.append(4)       # add 4 to lst1
print(lst1)          # prints [1, 2, 3, 4]
print(lst2)          # prints [1, 2, 3, 4] (same list as lst1)

