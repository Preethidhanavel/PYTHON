'''Write a function factorial(n) that uses recursion to calculate the factorial of a number'''
# Function to calculate factorial using recursion
def factorial(n):
    if n == 0:       # Base case: factorial of 0 is 1
        return 1
    return n * factorial(n - 1)  # Recursive call

# Input number from user
n = int(input("Enter the number: "))

# Call factorial function and print result
print(f"The factorial of {n} is {factorial(n)}")
