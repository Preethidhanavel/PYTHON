'''Execute Code Stored in a String
Explanation: Run the code present in the string (useful but risky if input is untrusted).
Input: "print(5+2)"
Expected Output: 7'''
s=input("Enter the code stored in a string:")
exec(s)