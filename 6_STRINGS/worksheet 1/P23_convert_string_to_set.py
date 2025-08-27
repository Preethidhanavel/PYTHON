'''Convert a String to a Set (Unique Characters)
Explanation: Keep only unique characters from the string.
Input: "balloon"
Expected Output: {'b', 'a', 'l', 'o', 'n'}'''
# Function to convert string into a set of unique characters
def str_set(s):
    seen = []               # List to keep track of characters already seen
    for i in s:
        if i not in seen:   # Add only if not already present
            seen.append(i)
    return set(seen)        # Convert list to set and return


# Take input from user
s = input("Enter the string: ")

# Print result (set of unique characters)
print(str_set(s))
