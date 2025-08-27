'''Print the Middle Character of a String
Explanation: Display the character(s) at the center of the string.
Input: "python"
Expected Output: Middle character: 't' and 'h' '''
# Function to find the middle character(s) of a string
def find_mid(s):
    mid = len(s) // 2   # Find middle index
    
    # If length is even, print two middle characters
    if len(s) % 2 == 0:
        print(s[mid - 1], s[mid])
    else:
        # If length is odd, print single middle character
        print(s[mid])


# Take input from user
s = input("Enter the string: ")

# Call the function
find_mid(s)
