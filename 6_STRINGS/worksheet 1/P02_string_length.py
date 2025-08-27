'''Find the Length of a String
Explanation: Count the total characters (including spaces) in a string.
Input: "hello world"
Expected Output: Length: 11'''
# Function to calculate length of a string without using len()
def my_len(s):
    c = 0                      # Initialize counter
    for i in s:                # Iterate through each character
        c += 1                 # Increment counter
    return c                   # Return total count

# Input string from user
s = input("Enter the string:")

# Call function and print length
print("The length is: ", my_len(s))
