#Count the Number of 1 Bits in an Integer (No Loops)
#Write an expression (using built-in functions) to count how many 1s are in the binary representation of a number.
#Sample Input: n = 29
# Take an integer input from the user
n = int(input("Enter the num: "))

# Convert the number to binary string 
print(bin(n).count('1'))

# Store the binary representation of the number as a string 
x = bin(n)

# Print the binary form of the number
print(x)
