'''Check if the input number reads the same backward as forward, using only loops and arithmetic.'''
# Take an integer input from user
n = int(input("Enter an integer: "))

# Check if the number is negative
negative = n < 0

# Work with absolute value for palindrome check
n = abs(n)

# Initialize variable to store reversed number
s = 0

# Store original number for comparison
original = n

# Loop to reverse the digits
while n > 0:
    digit = n % 10     
    s = s * 10 + digit   
    n = n // 10          

# Check if original number equals reversed number
if s == original:
    print("True")         # Palindrome
else:
    print("False")        # Not a palindrome

# Indicate if original number was negative
if negative:
    print("\n(Note: Original number was negative)")
