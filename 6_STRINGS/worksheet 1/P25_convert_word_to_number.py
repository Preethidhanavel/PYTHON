'''Convert Numeric Words to Actual Numbers
Explanation: Replace words like 'one', 'two' with their numeric equivalents.
Input: "I have one apple and two oranges."
Expected Output: "I have 1 apple and 2 oranges."'''
# Function to replace number words with digits
def replace(s):
    # Split the input string into words
    l = s.split()
    print(l)   #  show the list of words

    # Dictionary mapping number words to digits
    d = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9', 'ten': '10'
    }

    res = []  # List to store processed words/numbers
    
    # Loop through each word in the string
    for i in l:
        if i.lower() in d:       # Check if word is in dictionary
            num = d[i.lower()]   # Replace word with corresponding digit
            res.append(num)
        else:
            res.append(i)        # Keep the word unchanged if not in dictionary
    
    print(res)   #  show the list after replacement
    return ' '.join(res)   # Join back into a sentence


# Take user input
s = input("Enter the string: ")
print("After replacement:", replace(s))

            