'''Eliminate Duplicate Characters from a String
Explanation: Log Session a new string containing only the first occurrence of each character.
Input: "programming"
Expected Output: "progamin"'''
# Function to remove duplicate characters from a string
def eliminate_dup(s):
    print("Original list:", s)  # Print original list of characters
    seen = []                   # List to store unique characters

    # Iterate through each character
    for i in s:
        if i not in seen:       # If character not already in seen
            seen.append(i)      # Add it to seen

    # Join unique characters back into a string
    return ''.join(seen)

# Input string from user
s = input("Enter the string: ")

# Convert string to list and remove duplicates
print(f"After removing the repeated characters: {eliminate_dup(list(s))}")
