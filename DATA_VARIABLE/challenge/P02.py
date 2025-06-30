#Explain the difference between mutable and immutable data types in Python, with practical examples.
#immutable
a = 10
b = a
a = a + 5
print(a)  
print(b)  

#mutable
lst1 = [1, 2, 3]
lst2 = lst1
lst1.append(4)
print(lst1)
print(lst2)  
