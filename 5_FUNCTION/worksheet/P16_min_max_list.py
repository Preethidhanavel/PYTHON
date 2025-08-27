'''Write a function min_max(numbers) that returns both the smallest and largest number in a list (use returning multiple values).
'''
# Function to find minimum and maximum in a list
def min_max(l):
    min = l[0]  # Initialize min with first element
    max = l[0]  # Initialize max with first element
    for i in l:
        if i > max:   # Update max if current element is greater
            max = i
        if i < min:   # Update min if current element is smaller
            min = i
    return min, max

# Input numbers from user
n = input("Enter numbers separated by spaces: ")

# Convert input string into list of integers
l = list(map(int, n.split()))
print("List:", l)

# Call min_max function and unpack results
min_val, max_val = min_max(l)
print(f"The minimum and maximum in list is {min_val}, {max_val}")
