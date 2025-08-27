'''Take an 8-bit register value and print if the **MSB** (most significant bit) is set or not.
Input: 0b10010010
Output: MSB set
'''
# Take input as an 8-bit binary string (example: "10110011")
reg = input("Enter the 8 bit register value: ")

# Convert binary string (base 2) to integer
x = int(reg, 2)

# Check if the Most Significant Bit (MSB) is set
if x & 0b10000000:
    print("MSB set")
else:
    print("MSB not set")

