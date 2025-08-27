'''Check if Two Strings are Rotationally Equivalent
Explanation: Check if one string can be rotated (circularly shifted) to match the other.
Input: "abcde", "cdeab"
Expected Output: Rotationally equivalent: Yes'''
def rotation_eq(s1, s2):
    # Concatenate the string with itself
    s = s1 + s1
    
    # Check if s2 exists inside the doubled string
    n = s.find(s2)
    
    if n != -1:   # If found, it's a rotation
        print('Yes')
    else:         # Otherwise, it's not a rotation
        print('No')

# Take input from user
s1 = input("Enter the string1: ")
s2 = input("Enter the string2: ")

# Call the function
rotation_eq(s1, s2)
