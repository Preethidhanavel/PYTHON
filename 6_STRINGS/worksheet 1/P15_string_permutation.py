'''Generate All Permutations of a String
Explanation: List all possible ways to rearrange the characters.
Input: "abc"
Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']'''
# Recursive function to generate all permutations of a string
def permute(i, s, res):
    # Base case: if index reaches the end, store the permutation
    if i == len(s):
        res.append("".join(s))   # Join list into string
        return
 
    # Swap each character and recurse
    for j in range(i, len(s)):
        s[i], s[j] = s[j], s[i]      # Swap characters
        permute(i + 1, s, res)       # Recurse for next index
        s[i], s[j] = s[j], s[i]      # Backtrack (undo swap)


# Wrapper function to handle input and sorting
def permutation(s):
    res = []
    permute(0, list(s), res)   # Call recursive function
    res.sort()                 # Sort results (lexicographic order)
    return res


# Take user input
n = input("Enter the string: ")

# Generate permutations
r = permutation(n)

# Print all permutations
print(r)

