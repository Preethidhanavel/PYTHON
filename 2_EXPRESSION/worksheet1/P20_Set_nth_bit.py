#Set the nth Bit of a Number
#Write an expression that sets the nth bit of a given integer to 1 (leave other bits unchanged).
#Sample Input: n = 9, bit_position = 3
# Take an integer input from the user
n = int(input("Enter the number: "))

# Take the bit position input from the user
pos = int(input("Enter the position: "))

# Print the number in binary and decimal form before setting the bit
print(f"Before setting the bit {pos} position", bin(n), n)

# Set the bit at the given position 
x = n | (1 << pos)

# Print the number in binary and decimal form after setting the bit
print(f"After setting the bit {pos} position", bin(x), x)
