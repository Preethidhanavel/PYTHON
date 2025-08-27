'''Question: Write a function multiply(x, y) that returns the product of its two arguments'''
# Function to multiply two numbers
def multiply(x: int, y: int) -> int:
    return x * y

# Take two numbers as input
n = int(input("Enter the num1: "))
m = int(input("Enter the num2: "))

# Print the product of the two numbers
print("The product is: ", multiply(n, m))
