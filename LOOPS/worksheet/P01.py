'''Print all 3-digit numbers such that the sum of the cubes of their digits equals the number itself.
Example: 153 → 1³ + 5³ + 3³ = 153'''
for num in range(100, 1000):
    n = num
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10
    if total == num:
        print(num)
