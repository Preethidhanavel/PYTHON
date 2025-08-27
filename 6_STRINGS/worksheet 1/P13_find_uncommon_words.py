'''Find Uncommon Words Between Two Strings
Explanation: List words present in only one of the two strings.
Input: "red blue green", "blue yellow red"
Expected Output: Uncommon words: ['green', 'yellow']'''
# Function to find uncommon words in two strings
def find_uncommon(s1, s2):
    # Combine both strings into one
    s = s1 + ' ' + s2
    
    # Split combined string into list of words
    s = list(s.split())
    
    l = []  # List to store uncommon words
    
    # Check each word's frequency
    for word in s:
        if s.count(word) == 1:   # Word occurs only once in total
            l.append(word)
    
    return l  # Return the list of uncommon words


# Take input strings from user
s1 = input("Enter the string s1: ")
s2 = input("Enter the string s2: ")

# Print result
print("Uncommon words:", find_uncommon(s1, s2))
