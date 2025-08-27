'''Take an integer input and print its digits in reverse order (don’t use slicing or strings).'''
# Take an integer input from user
n = int(input("Enter an integer: "))

# Check if the number is negative
negative = n < 0

# Work with absolute value for reversing digits
n = abs(n)

print("Reversed digits:")

# Loop to extract and print digits in reverse order
while n > 0:
    digit = n % 10        
    print(digit, end=' ') 
    n = n // 10           

# Indicate if original number was negative
if negative:
    print("\n(Note: Original number was negative)")

