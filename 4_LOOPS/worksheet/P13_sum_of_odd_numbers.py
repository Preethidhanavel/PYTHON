'''Print the sum of all odd numbers from 1 up to n (inclusive), using loops only.'''
# Take input for the range
n = int(input("Enter the number range n:"))

# Initialize sum
sum = 0

# Loop through all odd numbers from 1 to n
for i in range(1, n + 1, 2):
    sum += i   # Add odd number to sum

# Print the sum of odd numbers
print("Sum of odd numbers:", sum)

