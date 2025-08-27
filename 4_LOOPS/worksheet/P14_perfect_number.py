'''Check if a given number is a perfect number (sum of divisors excluding itself), using only loops.'''
# Take input from the user
n = int(input("Enter the number: "))
n1 = n  # Store original number
sum = 0  # Initialize sum of factors

# Find all factors of n (excluding itself) and add them
for i in range(1, n):
    if n % i == 0:
        sum += i

# Check if sum of factors equals the original number
if sum == n1:
    print(f"The number {n1} is perfect")
else:
    print(f"The number {n1} is not perfect")
