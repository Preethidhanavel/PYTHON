'''Question: Write a recursive function fibonacci(n) that returns the nth Fibonacci number'''
# Function to calculate nth Fibonacci number recursively
def fibonacci(n):
    if n == 0:            # Base case: 0th Fibonacci number
        return 0
    elif n == 1:          # Base case: 1st Fibonacci number
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive calculation

# Input number from user
a = int(input("Enter the number: "))

# Call fibonacci function and print the result
print(f"The {a}th Fibonacci number is {fibonacci(a)}")
