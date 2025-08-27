'''Generate a Random Binary String
Explanation: Log Session a string of a given length containing only random 0s and 1s.
Input: Length = 8
Expected Output: e.g., "10101001"'''

import random

# Function to generate a random binary string of length p
def rand_key(p):
    key1 = ""   # Initialize empty string
    
    # Loop runs 'p' times to generate each bit
    for i in range(p):
        # Generate either 0 or 1 randomly
        temp = str(random.randint(0, 1))
        key1 += temp   # Append the bit to the string
        
    return key1   # Return the final binary string


# Take input from the user for length
n = int(input("Enter the length: "))

# Generate binary string of given length
str1 = rand_key(n)

# Display the result
print("Desired length random binary string is:", str1)
