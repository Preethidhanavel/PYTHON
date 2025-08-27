'''Remove Redundant Substrings from a List
Explanation: From a list of strings, remove repeated substring patterns.
Input: ["hellohello", "world", "testtesttest"]
Expected Output: ["hello", "world", "test"]'''

import ast

# Function to remove redundant repeated substrings
def remove_redundant_substrings(lst):
    res = []   # To store the result

    # Loop through each word in the list
    for word in lst:
        found = False
        # Check possible substring lengths (up to half the word length)
        for i in range(1, len(word) // 2 + 1):
            part = word[:i]  # Take a possible repeating part
            # If repeating this part forms the original word
            if part * (len(word) // len(part)) == word:
                res.append(part)  # Append only the base substring
                found = True
                break
        # If no repetition pattern found, keep the original word
        if not found:
            res.append(word)

    return res


# Take list input (example: ["abcabc", "aaaa", "xyz"])
test_list = input("Enter the list: ")

# Convert string input to actual Python list using ast.literal_eval
test_list = ast.literal_eval(test_list)

# Call function to process list
output_list = remove_redundant_substrings(test_list)

# Print final output
print("Filtered Output:", output_list)

