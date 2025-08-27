'''Remove the i-th Character from a String
Explanation: Remove the character at a given index in a string (starting from 0).
Input: String = "Python", i = 2
Expected Output: "Pythn"'''
# Function to remove character at index i from string
def remove_ith(s, i):
    return s[:i] + s[i+1:]   # Concatenate part before i and after i

# Input string from user
s = input("Enter the string: ")

# Input index to remove
i = int(input("Enter the index position:"))

# Print string after removing ith character
print(f"After removing {i} character from string: {remove_ith(s, i)}")
