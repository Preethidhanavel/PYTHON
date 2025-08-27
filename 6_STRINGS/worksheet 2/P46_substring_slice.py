'''Remove After a Substring
Explanation: Remove everything after a given substring in a s.
Input: String = "abcdeFGhiJK", Substring = "FG"
Expected Output: "abcdeFG"'''
# Take main string input
s = input("Enter the s:")

# Take substring input
s1 = input("Enter the substring:")

# Find the first occurrence index of substring in main string
index = s.find(s1)

# If substring is found (index != -1)
if index != -1:
    # Slice string from beginning up to the end of the found substring
    result = s[:index + len(s1)]
else:
    # If not found, keep original string
    result = s 

# Print final result
print("Output:", result)

