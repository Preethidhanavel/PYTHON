'''Replace Multiple Words at Once
Explanation: Simultaneously replace several different words in a string with new ones.
Input: String = "I like apples and bananas.", Replace: {"apples": "oranges", "bananas": "grapes"}
Expected Output: "I like oranges and grapes."'''
import ast

# Take a string input from the user
s = input("Enter the string: ")

# Take a dictionary input (for word replacement)
d = input("Enter the dict for replacement: ")

# Convert the string input into a Python dictionary safely
d = ast.literal_eval(d)

# Split the string into words
s = s.split()
print(s)  # Print list of words for reference

res = ''  # Initialize empty result string

# Traverse each word in the string
for i in s:
    if i in d:  # If the word is in the dictionary
        w = d.get(i)  # Get the replacement word
        res += ' ' + w  # Add replacement to result
    else:
        res = res + ' ' + i  # Otherwise, keep original word

# Print the final replaced string
print(res)
