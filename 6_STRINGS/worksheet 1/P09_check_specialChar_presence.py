'''Check if a String Contains Special Characters
Explanation: Check if the string contains characters other than letters or numbers.
Input: "Hello@123"
Expected Output: Contains special character: Yes'''
# Function to check if a string contains any special character
def check_spl(s):
    for i in s:
        # Check if the character is NOT an alphabet, digit, or space
        if not (i.isalpha() or i.isdigit() or i == ' '):
            return True   # Special character found
    return False  # No special character found


# Take input from the user
s = input("Enter the string: ")

# Print result (yes/no)
print("Contain special character:", 'yes' if check_spl(s) else 'no')
