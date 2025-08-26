'''Description: Given a string, convert it to a tuple of its characters, treating each character as an element.
This exercise is handy for data parsing and for character-level processing of strings.
Input: s = "python"
Output: ('p', 'y', 't', 'h', 'o', 'n')'''
s=input("Enter the string:")
print(tuple(s))
l=[]
for i in s:
    l.append(i)
print(tuple(l))