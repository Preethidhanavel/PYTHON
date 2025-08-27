'''For n rows, print a right-aligned triangle pattern:'''
# Take input for number of rows
n = int(input("Enter the number of rows:"))

# Loop through each row
for i in range(n):
    # Print spaces before stars
    print(' ' * (n - i - 1), end="")
    # Print stars for current row
    print("*" * (i + 1))
