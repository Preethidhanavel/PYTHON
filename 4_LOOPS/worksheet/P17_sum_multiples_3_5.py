'''Using only loops and arithmetic, compute the sum of all numbers below 1000 that are multiples of 3 or 5.'''
# Initialize sum
sum = 0

# Loop through numbers from 1 to 999
for i in range(1, 1000):
    # Check if the number is divisible by 3 or 5
    if i % 3 == 0 or i % 5 == 0:
        sum += i  # Add number to sum

# Print the final sum
print("Sum of all numbers below 1000 that are multiples of 3 or 5 is:", sum)
