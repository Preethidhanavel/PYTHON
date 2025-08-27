'''Implement a function permutations(s) that returns all unique permutations of a given string s. 
The result should be a list of strings.'''
# Recursive function to generate all permutations of a list of characters
def permute(i, s, res):
    if i == len(s):           # Base case: if index reaches end, append permutation
        res.append("".join(s))
        return
 
    for j in range(i, len(s)):
        s[i], s[j] = s[j], s[i]  # Swap characters at positions i and j
        permute(i + 1, s, res)   # Recurse for next index
        s[i], s[j] = s[j], s[i]  # Backtrack (restore original order)

# Function to generate sorted permutations of a string
def permutation(s):
    res = []
    permute(0, list(s), res)  # Start permutation with index 0
    res.sort()                 # Sort the results lexicographically
    return res

# Read input string from user
n = input("Enter the string:")

# Generate permutations
r = permutation(n)

# Print all permutations
print(r)
