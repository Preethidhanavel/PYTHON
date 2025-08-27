'''Enter a 16-bit value and print if parity (number of 1s) is even or odd.
Input: 0xAAAA
Output: Parity: Even'''
# Take a 16-bit hexadecimal value as input from the user
n = input("Enter a 16 bit value: ")

# Convert hexadecimal string to integer
x = int(n, 16)
print(x)        # Print the integer value

# Convert integer to binary string
b = bin(x)
#print Result
print("zero" if x == 0 else "Even" if (b.count('1') % 2 == 0) else "Odd")

