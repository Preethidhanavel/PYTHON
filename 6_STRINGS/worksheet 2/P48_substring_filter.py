'''Filter Strings with a Combination of k Substrings
Explanation: From a list, select only the strings that contain all of a set of k substrings.
Input: List = ["applebanana", "apple", "banana", "applebananacherry"], Substrings = ["apple", "banana"]
Expected Output: ["applebanana", "applebananacherry"]'''



# Define the original list of strings
test_list = ["applebanana", "apple", "banana", "applebananacherry"]
print("The original list:", test_list)

# Define the list of substrings we want to check
substr_list = ["apple", "banana"]

# Result list to store matched strings
res = []

# Loop through each string in the list
for s in test_list:
    # Check if ALL substrings in substr_list are present in the string 's'
    if all(sub in s for sub in substr_list):
        res.append(s)   # If yes, add it to result list

# Print the final filtered list
print("Strings after joins:", res)
