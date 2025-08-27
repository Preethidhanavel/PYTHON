'''Print all 3-digit numbers such that the sum of the cubes of their digits equals the number itself.
Example: 153 → 1³ + 5³ + 3³ = 153'''
# Loop through all 3-digit numbers
for num in range(100, 1000):
    n = num
    total = 0
    # Calculate sum of cubes of digits
    while n > 0:
        digit = n % 10       
        total += digit ** 3   
        n //= 10              

    # Check if sum of cubes equals the original number
    if total == num:
        print(num)               # Print the number

