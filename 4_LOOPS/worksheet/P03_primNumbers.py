'''Using only loops, print all prime numbers between 2 and n (n is user input).'''
# Take input from user
n = int(input("Enter the value of n: "))

# Loop through numbers from 2 to n
for num in range(2, n + 1):
    is_prime = True  # Assume number is prime
    # Check if number is divisible by any number from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # Not a prime number
            break  # Exit the inner loop early
    # If number is prime, print it
    if is_prime:
        print(num)

