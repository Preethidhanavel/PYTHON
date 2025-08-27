#Given an integer n, write an expression that is True if n is odd.
# Take input from user and convert to integer
n = int(input("Enter the n: "))

# Check if n is odd using modulus (%) operator
print("True" if n % 2 else "False")
