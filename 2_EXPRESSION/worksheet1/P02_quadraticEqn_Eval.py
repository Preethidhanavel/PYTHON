#Evaluate a Quadratic Expression
#Given values for x, a, b, and c, write an expression to compute ax² + bx + c.
#Sample Input: a = 2, b = 3, c = 4, x = 5
# Take input values for coefficients a, b, and c
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

# Take input value for variable x
x = int(input("Enter the value of x: "))

# Calculate the quadratic expression
y = (a * x**2) + (b * x) + c

# Print the final result
print("The result: ", y)
