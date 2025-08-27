'''Find Close Matches for a String in a List
Explanation: Find list entries that are similar to the given word (helpful for typo correction).
Input: Target = "apple", List = ["apply", "apples", "ape", "maple"]
Expected Output: Close matches: ['apply', 'apples']'''
import ast
import difflib

# Take input list as string and safely convert it to a Python list
list = input("Enter the list: ")
list = ast.literal_eval(list)   # Example input: ['apple','app','application']

# Take target string
t = input("Enter the target: ")

# ---- Method 1: Prefix Matching ----
l = []
for i in list:
    # If target starts with list item OR list item starts with target
    if t.startswith(i) or i.startswith(t):
        l.append(i)
print(l)  # Print all prefix matches

# ---- Method 2: Close Matches using difflib ----
close_matches = difflib.get_close_matches(t, list, n=3, cutoff=0.8)
print(close_matches)  # Print top 3 close matches (similar words)

# ---- Method 3: Manual substring check ----
for i in list:
    if t[:len(i)] == i or i[:len(t)] == t:
        print(i)  # Print matches based on slicing comparison
