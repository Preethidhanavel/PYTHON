'''Split String into Groups of n Characters
Explanation: Divide a string into equal-sized chunks.
Input: "abcdefgh", n = 3
Expected Output: ['abc', 'def', 'gh']'''
# Function to split string into chunks of size n
def split_into_chunks(s, n):
    l = []  # List to store chunks
    # Loop through string in steps of n
    for i in range(0, len(s), n):
        l.append(s[i:i+n])   # Extract substring of length n and add to list
    return l

# Input string from user
s = input("Enter the string: ")

# Input chunk size from user
n = int(input("Enter the chunk size: "))

# Call function to split string into chunks
result = split_into_chunks(s, n)

# Print the result
print("Chunks:", result)

