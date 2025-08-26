'''Print Superscript and Subscript in String Output
Explanation: Show part of the string as superscript or subscript, for math or scientific notation.
Input: "E = mc2" (display 2 as superscript)
Expected Output: "E = mc²"'''

superscript_map = {'0': '\u2070', '1': '\u00B9', '2': '\u00B2', '3': '\u00B3','4': '\u2074', '5': '\u2075', '6': '\u2076', '7': '\u2077',
    '8': '\u2078', '9': '\u2079'}


subscript_map = {'0': '\u2080', '1': '\u2081', '2': '\u2082', '3': '\u2083','4': '\u2084', '5': '\u2085', '6': '\u2086', '7': '\u2087',
    '8': '\u2088', '9': '\u2089'}

text = input("Enter the expression (e.g., H2O or E=mc2): ")
mode = input("Choose mode ('sup' for superscript, 'sub' for subscript): ").strip().lower()

result = ""

for ch in text:
    if ch.isdigit():
        if mode == "sup":
            result += superscript_map[ch]
        elif mode == "sub":
            result += subscript_map[ch]
        else:
            result += ch  
    else:
        result += ch

print("Formatted Output:", result)



