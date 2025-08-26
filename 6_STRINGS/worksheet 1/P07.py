'''Identify the Least Frequent Character in a String
Explanation: Find the character(s) that occur(s) the fewest times in a string.
Input: "statistics"
Expected Output: Least frequent character: 'a' '''
def least_freq(s):
    f=[0]*256
    for i in s:
        f[ord(i)]+=1
    min=f[ord(s[0])]
    c=s[0]
    for i in s:
        if min>f[ord(i)]:
            min=f[ord(i)]
            c=i
    return c
s=input("Enter the string: ")
print(f"The character having least frequency {least_freq(s)}")
d={}
ma=100000
char=s[0]
for i in s:
    d[i]=s.count(i)
    if d[i] < ma:
        ma=d[i]
        char =i
print(char,ma)