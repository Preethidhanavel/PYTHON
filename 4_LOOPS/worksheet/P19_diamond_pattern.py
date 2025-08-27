'''For n rows, print the following double triangle pattern:'''
# Read the number of rows 
n = int(input("Enter the number of rows (odd number): "))

# Calculate the middle row
mid = (n + 1) // 2  

# Print the upper half of the pattern
for i in range(1, mid + 1):
    print('*' * i)  # Print i stars

# Print the lower half of the pattern
for i in range(mid - 1, 0, -1):
    print('*' * i)  # Print i stars
