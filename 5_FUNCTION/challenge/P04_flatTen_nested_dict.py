'''Write a recursive function flatten_dict(d, p='', s='_') that takes a nested dictionary and flattens it, 
so that the result is a single-level dictionary with keys as the path joined by s.'''
import ast

# Function to flatten a nested dictionary
def flatten_dict(d, p='', s='_'):
    flat_dict = {}  
    for key, value in d.items():
        # Create new key name, append parent prefix if exists
        n = f"{p}{s}{key}" if p else key
        if isinstance(value, dict):  # If value is a dictionary, recurse
            flat_dict.update(flatten_dict(value, n, s))
        else:                        # Otherwise, store value in flat_dict
            flat_dict[n] = value
    return flat_dict

# Input nested dictionary from user as a string
n = input("Enter a nested dictionary (e.g., {'a': 1, 'b': {'c': 2}}): ")

# Convert input string to actual dictionary
d = ast.literal_eval(n)
print("Your nested dictionary:", d)

# Flatten the dictionary
d1 = flatten_dict(d)
print(d1)
