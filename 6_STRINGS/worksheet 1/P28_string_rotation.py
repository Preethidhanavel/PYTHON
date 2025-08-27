'''Rotate a String by k Positions
Explanation: Shift characters in the string to the right by k positions.
Input: String = "hello", k = 2
Expected Output: "lohel"'''
# Take input string from user
s = input("Enter the string: ")

# Take number of rotations from user
k = int(input("Enter the number of rotation: "))

# To avoid unnecessary full rotations, take modulo with string length
k = k % len(s)

# Perform rotation: take last k characters and move them to the front
s = s[-k:] + s[:-k]

# Print the rotated string
print("After rotation: ", s)