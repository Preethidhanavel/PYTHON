#Given a = 4, b = 5, write expressions to calculate their sum and product in a single line.
# Take input from user for variable a
a = int(input("Enter the a: "))

# Take input from user for variable b
b = int(input("Enter the b: "))

# Calculate sum and product using tuple assignment
x, y = a + b, a * b

# Print the results
print("sum:", x, "product:", y)
