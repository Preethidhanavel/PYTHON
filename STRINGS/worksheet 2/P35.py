'''Remove Punctuation from a String
Explanation: Remove all punctuation marks, keeping only letters, digits, and spaces.
Input: "Hello, world! How are you?"
Expected Output: "Hello world How are you"'''
import string
s=input("Enter the string:")
res=''
for i in s:
    if i not in string.punctuation:
        res+=i
print(res)