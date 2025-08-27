'''Input a number and find its smallest divisor greater than 1 (using only loops).'''
# Read the number from user
n = int(input("Enter the number: "))

# Loop from 2 to n to find the smallest divisor
for i in range(2, n + 1):
    if n % i == 0:          # Check if i divides n
        print(f"The smallest divisor of {n} is", i)
        break               # Stop after finding the first (smallest) divisor
