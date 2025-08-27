'''Reverse Sort a String
Explanation: Sort the characters of the string in descending order.
Input: "python"
Expected Output: "ytponh"'''
# Take input string from the user
s = input("Enter the string: ")

# Sort the string characters in descending order (reverse=True)
s1 = sorted(s, reverse=True)

# Join the sorted list back into a string and print
print(''.join(s1))
