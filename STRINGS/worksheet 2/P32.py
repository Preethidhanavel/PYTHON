'''Find the Position of a Character in the k-th Word
Explanation: Given a list of strings, find the position of a specific character in the k-th word.
Input: List = ["hello", "world"], k = 2, char = "r"
Expected Output: Position: 2'''
import ast
l=input("Enter the list:")
l=ast.literal_eval(l)
k=int(input("Enter the word number position:"))
c=input("Enter the character:")
for i in range(0,len(l)):
    pos=-1
    if i==k-1:
        pos=l[i].find(c)
        break
print("the posiiton :",pos)

