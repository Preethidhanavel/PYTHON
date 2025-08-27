'''Mirror Image of a String
Explanation: Reverse the string as if viewing in a mirror.
Input: "abcd"
Expected Output: "dcba"'''
def mirror_image(s):
    res = ''  
    # Loop from last character to first character
    for i in range(len(s) - 1, -1, -1):
        res += s[i]  # Append each character in reverse order
    return res

# Take input string from user
s = input("Enter the string: ")

# Print the mirror image (reversed string)
print(mirror_image(s))
