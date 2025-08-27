'''Input a number and count how many digits it contains, using only arithmetic and loops.'''
# Take input integer from user
n = int(input("Enter an integer: "))

# Check if the number is negative
negative = n < 0

# Work with absolute value
n = abs(n)

# Initialize counter for digits
c = 0

print("Reversed digits:")

# Count digits by extracting each digit
while n > 0:
    digit = n % 10       
    c += 1               
    n = n // 10           

# Print total number of digits
print(c)
