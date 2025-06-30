'''Find Uncommon Words Between Two Strings
Explanation: List words present in only one of the two strings.
Input: "red blue green", "blue yellow red"
Expected Output: Uncommon words: ['green', 'yellow']'''
def find_uncommon(s1,s2):  #function to find uncommon owrds in two strings
    s=s1+' '+s2
    s=list(s.split())
    #print(s)
    l=[]
    for word in s:
        if s.count(word)==1:
            l.append(word)
    return l
s=input("Enter the string s1:")
s1=input("Enter the string s2:")
print("uncommon words:",find_uncommon(s,s1))