'''Write a recursive function sum_list(lst) to return the sum of all elements in a list'''
# Function to calculate sum of a list recursively
def sum_list(l):
    if not l:          # Base case: empty list sum is 0
        return 0
    return l[0] + sum_list(l[1:])  # Recursive sum of first element + rest

# Input numbers from user and convert to list of integers
n = input("Enter numbers separated by spaces: ")
l = list(map(int, n.split()))

# Print the list
print("List:", l)

# Call sum_list function and print the sum
print(f"The sum of list: {sum_list(l)}")

