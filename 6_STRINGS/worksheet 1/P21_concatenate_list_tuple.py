'''Convert a List or Tuple of Characters to a String
Explanation: Combine list/tuple elements into a single string.
Input: ['p', 'y', 't', 'h', 'o', 'n']
Expected Output: "python"'''
import ast   # Import Abstract Syntax Trees for safe evaluation

# Take input from user (list or tuple as string)
s = input("Enter list or tuple: ")

# Convert input string into actual Python list/tuple safely
s1 = ast.literal_eval(s)

r = ''  # Empty string to store concatenated result

# Loop through each element and add to result
for i in s1:
    r += i

# Print final concatenated string
print("Output:", r)
