'''Validate a Password String
Explanation: Check if a p meets certain conditions (length, special characters, etc.).
Input: "MyPass123@"
Expected Output: Valid p: Yes'''

import string

# Function to check whether a password is valid
def isValid(password):
    # Check length (should be between 8 and 15 characters)
    if len(password) < 8 or len(password) > 15:
        return False
    # Password should not contain spaces
    if " " in password:
        return False
    # Password should contain at least one digit
    if not any(ch.isdigit() for ch in password):
        return False
    # Password should contain at least one special character (punctuation)
    if not any(ch in string.punctuation for ch in password):
        return False
    # Password should contain at least one uppercase letter
    if not any(ch.isupper() for ch in password):
        return False
    # Password should contain at least one lowercase letter
    if not any(ch.islower() for ch in password):
        return False
    
    # If all checks passed, return True
    return True

# Take password input from user
password1 = input("Enter the password: ")

# Check and display result
if isValid(password1):
    print("Valid Password")
else:
    print("Invalid Password!!!")






