'''Check if Two Strings are Rotationally Equivalent
Explanation: Check if one string can be rotated (circularly shifted) to match the other.
Input: "abcde", "cdeab"
Expected Output: Rotationally equivalent: Yes'''
def rotation_eq(s1,s2):
    s=s1+s1
    n=s.find(s2)
    if n !=-1:
        print('Yes')
    else:
        print('No')
s1=input("Enter the string1:")
s2=input("Enter the string2:")
rotation_eq(s1,s2)