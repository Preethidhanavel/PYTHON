'''Take an integer and, using only loops, sum its digits repeatedly until only a single digit remains.
Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2'''
# Take input number from user
n = int(input("Enter the number: "))

# Initialize sum to 0
sum = 0

# Repeat until the number becomes a single-digit number
while n > 0 or sum > 9:
    if n == 0:
        # Set n to sum and reset sum to 0
        n = sum
        sum = 0

    # Add last digit of n to sum
    sum += n % 10
    # Remove last digit from n
    n //= 10

# Print the final single-digit sum
print(sum)
