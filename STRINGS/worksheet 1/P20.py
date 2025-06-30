'''Split a String into a List of Characters
Explanation: Break the string into individual characters.
Input: "dog"
Expected Output: ['d', 'o', 'g']'''
def list_l(s):
    l=[]
    for i in s:
        l.append(i)
    print(l)
s=input("Enter the string:")
#print("output:",list(s))
list_l(s)