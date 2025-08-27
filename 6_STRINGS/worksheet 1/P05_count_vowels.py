'''Count Vowels in a String Using Sets
Explanation: Find how many vowels (a, e, i, o, u) are in the string, using sets for efficiency.
Input: "education"
Expected Output: Vowels Count: 5'''
# Function to count vowels in a string
def count_vowels(s):
    vowels = {'a','e','i','o','u'}  # Set of vowels
    n = s.lower()                   # Convert string to lowercase
    count = 0                       

    # Iterate through each character
    for char in n:
        if char in vowels:          # Check if character is a vowel
            count += 1
    return count

# Input string from user
s = input("Enter the string: ")

# Print number of vowels
print(f"The number of vowels are {count_vowels(s)}")
