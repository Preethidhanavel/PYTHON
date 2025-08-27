'''Reverse Words in a String
Explanation: Reverse the order of words in a sentence, not the letters.
Input: "I love Python"
Expected Output: "Python love I"'''
# Function to reverse the order of words in a string
def reverse_words(s):
    word = s.split()            # Split string into words
    reverse = ""                
    for w in word:
        reverse = w + " " + reverse  # Prepend each word to reverse string
    return reverse

# Input string from user
s = input("Enter the string:")

# Call function and print reversed words
print(f"After reversing words: {reverse_words(s)}")

# Alternative method using list slicing
w = s.split()
print(" ".join(w[::-1]))       # Join words in reversed order

