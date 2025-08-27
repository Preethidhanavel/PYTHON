'''Swap Commas and Dots in a String
Explanation: Replace commas with dots and dots with commas.
Input: "23,45.89,78.90"
Expected Output: "23.45,89.78,90"'''
# Function to swap symbols in a string
def swap(s):
    # Replace ',' with '!'
    s = s.replace(',', '!')
    
    # Replace '.' with ','
    s = s.replace('.', ',')
    
    # Replace '!' with '.'
    s = s.replace('!', '.')
    
    return s  # Return modified string


# Take input from user
s = input("Enter the string: ")

# Call function and print result
s1 = swap(s)
print(s1)
