'''Split a String into a List of Characters
Explanation: Break the string into individual characters.
Input: "dog"
Expected Output: ['d', 'o', 'g']'''
# Function to convert a string into a list of characters
def list_l(s):
    l = []              # Empty list to store characters
    for i in s:
        l.append(i)     # Append each character to the list
    print(l)            # Print the final list


# Take input from user
s = input("Enter the string: ")

# (Alternative built-in method: list(s))
# print("output:", list(s))

# Call the function
list_l(s)
