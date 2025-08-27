'''Check for Pangram
Explanation: Verify if a string contains every letter of the alphabet at least once.
Input: "The quick brown fox jumps over the lazy dog"
Expected Output: Is pangram: Yes'''
import string

# Input string from user
a = input("Enter the string: ")

# Create a set of all lowercase English letters (a-z)
b = set(string.ascii_lowercase)

# Convert input string to lowercase and make it a set (unique characters only)
s = set(a.lower())

# Check if all letters (a-z) are present in the input string
res = b <= s   # True if 'b' is subset of 's'
print(res)
