''' Write a function find_duplicates(lst) that returns a list of all elements that appear more than once in the input list. 
The result should contain no duplicates and preserve the order of their first appearance.'''
# Function to find all duplicates in a list
def find_duplicates(lst):
    seen = set()        # To track seen elements
    duplicates = set()  # To track duplicates already added to result
    result = []         # To store duplicate elements in order

    for item in lst:
        if item in seen:
            if item not in duplicates:  # Add only first duplicate occurrence
                result.append(item)
                duplicates.add(item)
        else:
            seen.add(item)  # First time seeing the item

    return result

# Read input from user as a space-separated string
a = input("Enter the list separated by spaces:")

# Convert input string into a list of integers
l = list(map(int, a.split()))

# Print the original list
print(l)

# Find duplicates in the list
x = find_duplicates(l)

# Print the list of duplicates
print(x)
