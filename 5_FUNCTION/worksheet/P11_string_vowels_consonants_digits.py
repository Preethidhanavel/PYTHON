''' Write a function string_stats(s) that returns the number of vowels, consonants, and digits in the string s'''
# Function to count vowels, consonants, and digits in a string
def string_stats(s):
    vowels = 'aeiouAEIOU'  # Define vowels
    v = 0   # Count of vowels
    c = 0   # Count of consonants
    d = 0   # Count of digits

    for char in s:
        if char.isdigit():    # Check if character is a digit
            d += 1
        elif char.isalpha():  # Check if character is alphabet
            if char in vowels:  # Check if vowel
                v += 1
            else:
                c += 1        # Else consonant

    return v, c, d  # Return counts

# Input string from user
n = input("Enter the string: ")

# Call function and get counts
a, b, c = string_stats(n)

# Print results
print(f"the number of vowels {a}, consonants {b}, digits {c}")
