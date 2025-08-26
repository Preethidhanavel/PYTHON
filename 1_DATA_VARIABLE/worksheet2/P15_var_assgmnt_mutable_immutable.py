#How does variable assignment differ between mutable and immutable objects? 
#Illustrate with an example.
#Mutable objects: both variables can reference the same object, and changes affect both.
#Immutable objects: assignment creates a new object on modification.

x = 5        # x is assigned integer value 5
y = x        # y also refers to the same integer value 5
print(x, y)  # prints 5 5

x = 10       # x is now updated to 10 (y is still 5, since integers are immutable)
print(x, y)  # prints 10 5

a = [1, 2, 3]   # a points to a list [1, 2, 3]
b = a           # b refers to the same list as a
print(a, b)     # prints [1, 2, 3] [1, 2, 3]

a[0] = 9        # modifies the first element of the list (affects both a and b)
print(a, b)     # prints [9, 2, 3] [9, 2, 3]
