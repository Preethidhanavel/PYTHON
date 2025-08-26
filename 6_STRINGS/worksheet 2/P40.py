'''Pad a String with Characters
Explanation: Add extra characters (like *, space, or 0) to the left or right of a string to reach a desired length.
Input: "cat", Length = 6, Pad char = "*"
Expected Output: "***cat" '''
s=input("Enter the string:")
l=int(input("Enter the desired length:"))
res=''
if l>=len(s):
    c=input("Enter the character to append")
    res=c*(l-len(s))
    res+=s
else:
    res=s
print(res)