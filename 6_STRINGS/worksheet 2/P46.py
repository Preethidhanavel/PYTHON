'''Remove After a Substring
Explanation: Remove everything after a given substring in a s.
Input: String = "abcdeFGhiJK", Substring = "FG"
Expected Output: "abcdeFG"'''
s=input("Enter the s:")
s1=input("Enter the substring:")

index = s.find(s1)

# If found, slice up to the end of the s1
if index != -1:
    result = s[:index + len(s1)]
else:
    result = s 

print("Output:", result)
