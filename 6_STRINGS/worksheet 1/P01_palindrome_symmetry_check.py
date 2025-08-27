'''Check if a String is a Palindrome or Symmetrical
Explanation: A palindrome reads the same forwards and backwards (e.g., "madam"). A symmetrical string has matching halves.
Input: "madam"
Expected Output:
Palindrome: Yes
Symmetrical: Yes'''

# Function to check if a string is palindrome and symmetrical
def check_pal_sym(s):
    mid = len(s) // 2               # Find middle index
    pal = s == s[::-1]              # Check if string is palindrome

    # Split string into left and right halves
    if len(s) % 2 == 0:             
        left = s[:mid]              
        right = s[mid:]             
    else:
        left = s[:mid]              
        right = s[mid+1:]           

    sym = left == right             # Check if halves are symmetrical

    return pal, sym

# Input string from user
s = input("Enter the string: ")

# Call function and store results
is_pal, is_sym = check_pal_sym(s)

# Print results
print("Palindrome:", "Yes" if is_pal else "No")
print("Symmetrical:", "Yes" if is_sym else "No")


