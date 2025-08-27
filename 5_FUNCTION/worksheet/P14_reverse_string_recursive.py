'''Write a recursive function reverse_string(s) that returns the reversed string'''
# Function to reverse a string recursively
def reverse_string(s):
    if len(s) <= 1:           # Base case: single character or empty string
        return s
    return s[-1] + reverse_string(s[:-1])  # Last char + reverse of rest

# Input string from user
s = input("Enter the string: ")

# Call reverse_string function and print the result
print(f"After reversing: {reverse_string(s)}")
