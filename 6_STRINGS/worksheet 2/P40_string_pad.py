'''Pad a String with Characters
Explanation: Add extra characters (like *, space, or 0) to the left or right of a string to reach a desired length.
Input: "cat", Length = 6, Pad char = "*"
Expected Output: "***cat" '''
# Take input string from the user
s = input("Enter the string: ")

# Take the desired final length of the string
l = int(input("Enter the desired length: "))

# Initialize result string
res = ''

# If desired length is greater than or equal to original string length
if l >= len(s):
    # Take the character to append
    c = input("Enter the character to append: ")
    # Append (l - len(s)) times the character before the original string
    res = c * (l - len(s))
    res += s
else:
    # If desired length is smaller, just keep the original string
    res = s

# Print the final string
print(res)
