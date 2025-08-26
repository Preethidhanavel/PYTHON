'''Rotate a String by k Positions
Explanation: Shift characters in the string to the right by k positions.
Input: String = "hello", k = 2
Expected Output: "lohel"'''
s=input("Enter the string:")
k=int(input("enter the number of rotation:"))
k=k%len(s)
s=s[-k:]+s[:-k]
print("After rotation: ",s)