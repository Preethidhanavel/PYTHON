'''Swap Commas and Dots in a String
Explanation: Replace commas with dots and dots with commas.
Input: "23,45.89,78.90"
Expected Output: "23.45,89.78,90"'''
def swap(s):
    s=s.replace(',','!')
    s=s.replace('.',',')
    s=s.replace('!','.')
    return s
s=input("Enter the string:")
s1=swap(s)
print(s1)