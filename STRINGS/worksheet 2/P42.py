'''Check for Pangram
Explanation: Verify if a string contains every letter of the alphabet at least once.
Input: "The quick brown fox jumps over the lazy dog"
Expected Output: Is pangram: Yes'''
import string

# Input string
a = input("Enter the string:")

# Create set of all lowercase English letters
b = set(string.ascii_lowercase)

s = set(a.lower())

res = b <= s
print(res)