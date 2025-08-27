'''Frequency of Consecutive Characters
Explanation: Count how many times each character repeats in sequence.
Input: "aabccddd"
Expected Output: {'a': 2, 'b': 1, 'c': 2, 'd': 3}'''
# Function to count frequency of each character in a string
def count_freq(s):
    f = {}  # Empty dictionary to store character counts
    for i in s:
        # If character exists, increase count; else set to 1
        f[i] = f.get(i, 0) + 1  
    print(f)  # Print the frequency dictionary

# Take input string from user
s = input("Enter the string:")

# Call the function
count_freq(s)