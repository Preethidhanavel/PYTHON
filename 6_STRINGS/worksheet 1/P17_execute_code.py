'''Execute Code Stored in a String
Explanation: Run the code present in the string (useful but risky if input is untrusted).
Input: "print(5+2)"
Expected Output: 7'''
# Take Python code as input (stored in a string)
s = input("Enter the code stored in a string: ")

# Execute the given code dynamically
exec(s)
