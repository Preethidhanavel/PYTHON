'''Find the Maximum Frequency Character
Explanation: Determine which character appears most frequently in the string.
Input: "banana"
Expected Output: Maximum frequency character: 'a' '''
# Function to find the character with maximum frequency
def maximum_freq(s):
    # Create a frequency list of size 256 (for ASCII characters)
    f = [0] * 256  
    
    # Count frequency of each character
    for i in s:
        f[ord(i)] += 1  
    
    # Initialize with frequency of the first character
    m = f[ord(s[0])]
    c = s[0]
    
    # Find the character with maximum frequency
    for i in s:
        if m < f[ord(i)]:   # Compare with current maximum
            m = f[ord(i)]   # Update maximum frequency
            c = i           # Update character
    
    return c  # Return the character having maximum frequency


# Take input from the user
s = input("Enter the string: ")

# Print result
print(f"The character having maximum frequency {maximum_freq(s)}")
