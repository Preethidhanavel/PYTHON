'''Reverse Words in a String
Explanation: Reverse the order of words in a sentence, not the letters.
Input: "I love Python"
Expected Output: "Python love I"'''
def reverse_words(s):
    word=s.split()
    reverse=""
    for w in word:
        reverse=w+" "+reverse
    return reverse
s=input("Enter the string:")
print(f"After reversing words:{reverse_words(s)}")
w=s.split()
print(" ".join(w[::-1]))
