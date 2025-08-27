'''Find the Location of a Word in a String
Explanation: Find the index where a word first appears in the string.
Input: String = "welcome to python", Word = "python"
Expected Output: Position: 11'''
# Take input string from user
s = input("Enter the string:")

# Take the word to search for
s1 = input("Enter word to find its position:")

# Use find() to get the position of the word (returns -1 if not found)
print("Output:", s.find(s1))
