#Given a number n, write an expression to get the last digit (units place) of n.
# Take input from user and convert to integer
n = int(input("Enter the n: "))

# Find the unit digit using modulus operator (%)

print(f"unit digit of {n} is", n % 10)
