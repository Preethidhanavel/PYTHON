'''Extract Indices of Substring Matches
Explanation: Find all starting positions of a substring in a s.
Input: String = "abracadabra", Substring = "abra"
Expected Output: [0, 7]'''
s=input("Enter the s:")
s1=input("Enter the substring:")
res = []
for i in range(len(s) - len(s1) + 1):
    if s[i:i+len(s1)] == s1:
        res.append(i)

print("Starting indices:", res)