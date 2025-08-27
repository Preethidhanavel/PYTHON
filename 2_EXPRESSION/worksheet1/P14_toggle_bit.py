#Toggle a Specific Bit in an Integer
#Given a number and a bit position, write an expression to toggle (flip) that bit.
#Sample Input: n = 12, bit_position = 2
# Take an integer input from the user
n = int(input("Enter the n: "))

# Take the bit position to toggle
position = int(input("Enter the position: "))


# XOR 
x = n ^ (1 << position)

# Print the new number after toggling the bit
print(x)
