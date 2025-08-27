'''Ask for two numbers and compute their Greatest Common Divisor (GCD) using repeated subtraction or division with loops.'''
# Take two integer inputs from user
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# Use absolute values for GCD calculation
a = abs(n1)
b = abs(n2)

# Method 1: Using repeated subtraction (Euclidean method)
while a != b:
    if a > b:
        a = a - b   # Subtract smaller from larger
    else:
        b = b - a

print("GCD (by subtraction method) is:", a)

# Reset a and b for next method
a = abs(n1)
b = abs(n2)

# Method 2: Using modulo operation 
while b != 0:
    temp = b
    b = a % b     # Remainder becomes new b
    a = temp      # Previous b becomes new a

print("GCD (by modulo method) is:", a)

