'''Find the Maximum Frequency Character
Explanation: Determine which character appears most frequently in the string.
Input: "banana"
Expected Output: Maximum frequency character: 'a' '''
def maximum_freq(s):
    f=[0]*256
    for i in s:
        f[ord(i)]+=1
    m=f[ord(s[0])]
    c=s[0]
    for i in s:
        if m<f[ord(i)]:
            m<f[ord(i)]
            c=i
    return c
s=input("Enter the string: ")
print(f"The character having maximum frequency {maximum_freq(s)}")