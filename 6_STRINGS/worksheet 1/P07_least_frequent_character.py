'''Identify the Least Frequent Character in a String
Explanation: Find the character(s) that occur(s) the fewest times in a string.
Input: "statistics"
Expected Output: Least frequent character: 'a' '''
# Function to find the least frequent character in a string
def least_freq(s):
    # Create a frequency list of size 256 (for ASCII characters)
    f = [0] * 256  
    
    # Count frequency of each character using ASCII values
    for i in s:
        f[ord(i)] += 1  
    
    # Initialize with the frequency of the first character
    min = f[ord(s[0])]
    c = s[0]
    
    # Find the character with the least frequency
    for i in s:
        if min > f[ord(i)]:
            min = f[ord(i)]
            c = i
    
    return c  # Return least frequent character


# Take input from user
s = input("Enter the string: ")

# Print result using first method
print(f"The character having least frequency {least_freq(s)}")


# ---- Another method using dictionary ----
d = {}          # Dictionary to store character counts
ma = 100000     # Large number as initial minimum frequency
char = s[0]     # Start with first character

# Count each character using dictionary
for i in s:
    d[i] = s.count(i)  # Count occurrences of i
    if d[i] < ma:      # Check if frequency is less than current minimum
        ma = d[i]
        char = i

# Print the least frequent character and its count
print(char, ma)
