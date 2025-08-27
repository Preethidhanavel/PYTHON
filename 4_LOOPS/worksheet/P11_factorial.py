'''Take a number as input and calculate its factorial using loops (no recursion).'''
# Take input number from user
n = int(input("Enter the number:"))

# Initialize factorial variable
f = 1

# Store original number for printing later
n1 = n

# Compute factorial using while loop
while n != 0:
    f = f * n  # Multiply current number
    n -= 1     # Decrement number

# Print the factorial
print(f"Factorial of {n1} is:", f)
