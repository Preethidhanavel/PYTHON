'''Reverse Sort a String
Explanation: Sort the characters of the string in descending order.
Input: "python"
Expected Output: "ytponh"'''
s=input("Enter the string:")
s1=sorted(s,reverse=True)
print(''.join(s1))