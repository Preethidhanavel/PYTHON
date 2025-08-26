'''Minimum Rotations to Get the Original String
Explanation: Count the rotations needed for a string to return to its original form.
Input: "abcde"
Expected Output: 5'''
def find_rotation(s):
    n = len(s)
    # Check if all characters are the same
    if s == s[0] * n:
        return 0
    for i in range(1, n):
        rotated = s[i:] + s[:i]
        if rotated == s:
            return i
    return 0

s=input("Enter the string:")
print(find_rotation(s))