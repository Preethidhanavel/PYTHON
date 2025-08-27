#Rotate Bits Left by k Positions
#Given a number (assume 8 bits) and a value k, write an expression to rotate its bits to the left by k positions.
#Sample Input: n = 150, k = 2
# Take an integer input from the user
n = int(input("Enter the number: "))

# Take how many positions to rotate
k = int(input("Enter the number of rotation: "))

# Limit k to the range [0, 31] because we assume 32-bit integer rotation
k = k % 32  

# Perform left rotation:
x = (n << k) | (n >> (32 - k))

# Print original number in binary format
print(bin(n))

# Print rotated number in binary format and also its decimal value
print(bin(x), " ", x)
