'''Remove Punctuation from a String
Explanation: Remove all punctuation marks, keeping only letters, digits, and spaces.
Input: "Hello, world! How are you?"
Expected Output: "Hello world How are you"'''
import string

# Take a string input from the user
s = input("Enter the string: ")

res = ''  # Initialize an empty result string

# Traverse each character in the input string
for i in s:
    # Check if the character is NOT punctuation
    if i not in string.punctuation:
        res += i  # Add the character to the result string

# Print the string after removing punctuation
print(res)
