''' Write a function calculate(a, b) that returns both the sum and difference of a and b'''
# Function to calculate sum and difference of two numbers
def calculate(a, b):
    sum = a + b        # Calculate sum
    diff = a - b       # Calculate difference
    return sum, diff   # Return both values

# Input two numbers
a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))

# Call the function and get sum and difference
x, y = calculate(a, b)

# Print results
print("Sum:", x)
print("Difference:", y)

