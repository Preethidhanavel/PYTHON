'''Find the Position of a Character in the k-th Word
Explanation: Given a list of strings, find the position of a specific character in the k-th word.
Input: List = ["hello", "world"], k = 2, char = "r"
Expected Output: Position: 2'''
import ast  

# Take list input from user (as string) and safely convert to Python list
l = input("Enter the list: ")
l = ast.literal_eval(l)

# Take the word position (1-based index)
k = int(input("Enter the word number position: "))

# Take the character to search for
c = input("Enter the character: ")

# Loop through the list
for i in range(0, len(l)):
    pos = -1  # Default position as -1 (not found)
    if i == k - 1:  # Check only the given word position
        pos = l[i].find(c)  # Find the character in that word
        break  # Stop after checking the required word

# Print the result
print("The position:", pos)


