'''Find all numbers less than 1000 which equal the sum of the factorials of their digits.
Valid Example: 145: 1! + 4! + 5! = 1 + 24 + 120 = 145 (valid)
Invalid Example: 123: 1! + 2! + 3! = 1 + 2 + 6 = 9 (not valid)'''
# Function to calculate factorial of a number
def fact(n):
    f = 1
    for i in range(n, 0, -1):  # Multiply all numbers from n down to 1
        f *= i
    return f

# Loop through numbers from 1 to 999
for i in range(1, 1000):
    n = i
    sum_val = 0
    # Calculate sum of factorials of digits
    while n != 0:
        r = n % 10             
        sum_val += fact(r)    
        n //= 10              

    # Check if sum of factorials equals the original number
    if sum_val == i:
        print(i, " ")           # Print matching number
