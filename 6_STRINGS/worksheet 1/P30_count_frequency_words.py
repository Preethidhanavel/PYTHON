'''Count Frequency of Words in String (Short Form)
Explanation: Show how many times each word appears.
Input: "apple apple orange"
Expected Output: {'apple': 2, 'orange': 1}'''
def count_word(s):
    # Split the string into words based on spaces
    s = s.split()

    # Dictionary to store word frequencies
    f = {}

    # Count each word using dictionary
    for i in s:
        f[i] = f.get(i, 0) + 1

    # Print the final word frequency dictionary
    print(f)

# Take input from user
s = input("Enter the string: ")

# Call the function
count_word(s)
