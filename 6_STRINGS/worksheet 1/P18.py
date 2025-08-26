'''Print the Middle Character of a String
Explanation: Display the character(s) at the center of the string.
Input: "python"
Expected Output: Middle character: 't' and 'h' '''
def find_mid(s):
    mid=len(s)//2
    if len(s)%2==0:
        print(s[mid-1],s[mid])
    else:
        print(s[mid])

s=input("Enter the string:")
find_mid(s)