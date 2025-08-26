#Can a Python variable change its data type after assignment? Give an example and explain the implications.
x = 10                     # Assign integer value 10 to variable x
print(x, type(x))          # Prints the value of x (10) and its type (<class 'int'>)

x = 3.14                   # Now x is reassigned to a floating-point number 3.14
print(x, type(x))          # Prints the value (3.14) and its type (<class 'float'>)

x = "hello"                # Now x is reassigned to a string "hello"
print(x, type(x))          # Prints the value (hello) and its type (<class 'str'>)

