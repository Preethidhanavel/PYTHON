#How do you convert between data types (e.g., string to int, int to float, list to tuple) in Python? Show a code example.
# String to Integer
s = "123"
i = int(s)
print(i, type(i))   

# Integer to Float
f = float(i)
print(f, type(f))   

# Float to Integer
print(int(5.9),type(int(5.9)))    

# Integer to String
print(str(456), type(str(456)))

# List to Tuple
lst = [1, 2, 3]
tup = tuple(lst)
print(tup, type(tup))  

# Tuple to List
tup2 = (4, 5, 6)
lst2 = list(tup2)
print(lst2, type(lst2))
