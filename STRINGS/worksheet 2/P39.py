'''Validate a Password String
Explanation: Check if a p meets certain conditions (length, special characters, etc.).
Input: "MyPass123@"
Expected Output: Valid p: Yes'''

import string

def isValid(password):
    if len(password) < 8 or len(password) > 15:
        return False
    if " " in password:
        return False
    if not any(ch.isdigit() for ch in password):
        return False
    if not any(ch in string.punctuation for ch in password):
        return False
    if not any(ch.isupper() for ch in password):
        return False
    if not any(ch.islower() for ch in password):
        return False
    return True


password1=input("Enter the password:")

if (isValid(password1)):
    print("Valid Password")
else:
    print("Invalid Password!!!")





