'''Minimum Rotations to Get the Original String
Explanation: Count the rotations needed for a string to return to its original form.
Input: "abcde"
Expected Output: 5'''
def find_rotation(s):
    n = len(s)
    # Check if all characters in the string are the same
    if s == s[0] * n:
        return 0

    # Try rotating the string from index 1 to n-1
    for i in range(1, n):
        rotated = s[i:] + s[:i]   # Rotate string at position i
        if rotated == s:          # If rotation brings back original string
            return i              # Return rotation index
    
    return 0  # If no rotation matches, return 0

# Take input from user
s = input("Enter the string: ")

# Print the result of rotation check
print(find_rotation(s))
