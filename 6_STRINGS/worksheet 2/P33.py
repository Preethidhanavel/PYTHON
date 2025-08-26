'''Mirror Image of a String
Explanation: Reverse the string as if viewing in a mirror.
Input: "abcd"
Expected Output: "dcba"'''
def mirror_image(s):
    res=''
    for i in range(len(s)-1,-1,-1):
        res+=s[i]
    return res
s=input("Enter the string:")
print(mirror_image(s))