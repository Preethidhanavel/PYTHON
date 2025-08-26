'''• Task: 
• Write a script that reads a text file and counts the occurrence of each word. 
• Validation: Verify that the output dictionary correctly represents word counts for 
given test files. '''
from collections import defaultdict
filename=input("Enter the filename:")
file=open(filename,"r")
content=file.read()

content=content.split()
d=defaultdict(int)
for i in content:
    d[i]+=1

print(d)
'''
import os
print("Current Working Directory:", os.getcwd())'''