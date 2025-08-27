'''Check If a String is a Binary String
Explanation: Test if the string contains only '0' and '1'.
Input: "101101"
Expected Output: Is binary string: Yes'''
# Function to check if a string is a valid binary string
def check_bin(s):
    # Check if all characters in the string are only '0' or '1'
    if set(s).issubset({'0', '1'}):
        return True
    return False


# Take input from user
s = input("Enter the binary string: ")

# Print result
print("Is binary string:", 'Yes' if check_bin(s) else 'No')
