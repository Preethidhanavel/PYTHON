'''Print Superscript and Subscript in String Output
Explanation: Show part of the string as superscript or subscript, for math or scientific notation.
Input: "E = mc2" (display 2 as superscript)
Expected Output: "E = mc²"'''
# Mapping of numbers to superscript Unicode characters
superscript_map = {
    '0': '\u2070', '1': '\u00B9', '2': '\u00B2', '3': '\u00B3',
    '4': '\u2074', '5': '\u2075', '6': '\u2076', '7': '\u2077',
    '8': '\u2078', '9': '\u2079'
}

# Mapping of numbers to subscript Unicode characters
subscript_map = {
    '0': '\u2080', '1': '\u2081', '2': '\u2082', '3': '\u2083',
    '4': '\u2084', '5': '\u2085', '6': '\u2086', '7': '\u2087',
    '8': '\u2088', '9': '\u2089'
}

# Take input expression from user
text = input("Enter the expression (e.g., H2O or E=mc2): ")

# Ask user whether to convert digits into superscript or subscript
mode = input("Choose mode ('sup' for superscript, 'sub' for subscript): ").strip().lower()

# Initialize empty result string
result = ""

# Loop through each character in the input
for ch in text:
    if ch.isdigit():  # If the character is a digit
        if mode == "sup":  # Convert to superscript
            result += superscript_map[ch]
        elif mode == "sub":  # Convert to subscript
            result += subscript_map[ch]
        else:  # If invalid mode, keep digit as it is
            result += ch  
    else:
        result += ch  # Non-digit characters remain the same

# Print the formatted output
print("Formatted Output:", result)



