#Can two different variables refer to the same object in Python? How can you check this?

x = [1, 2, 3]   # Create a list object in memory and assign it to variable x
y = x           # y now refers to the SAME list object as x 

print(x is y)   # True, because 'is' checks identity 
