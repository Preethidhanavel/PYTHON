'''Input n and print the nth Fibonacci number using only variable updates and a loop (no lists, no recursion).'''
# Read the number of Fibonacci terms
n = int(input("Enter the number: "))

# Initialize variables
i = 0
x, y, z = 0, 1, 0  # x and y store the last two Fibonacci numbers

# Generate Fibonacci sequence up to n terms
while i < n:
    z = x + y   # Next Fibonacci number
    x = y       # Shift x to y
    y = z       # Shift y to z
    i += 1

# Print the nth Fibonacci number
print(x)

