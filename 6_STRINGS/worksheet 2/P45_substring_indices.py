'''Extract Indices of Substring Matches
Explanation: Find all starting positions of a substring in a s.
Input: String = "abracadabra", Substring = "abra"
Expected Output: [0, 7]'''
# Take main string input
s = input("Enter the s:")

# Take substring input
s1 = input("Enter the substring:")

# List to store starting indices where substring is found
res = []

# Loop through string up to valid range
for i in range(len(s) - len(s1) + 1):
    # Check if substring matches at current position
    if s[i:i+len(s1)] == s1:
        res.append(i)  # Add starting index to result list

# Print all starting indices of substring in main string
print("Starting indices:", res)
