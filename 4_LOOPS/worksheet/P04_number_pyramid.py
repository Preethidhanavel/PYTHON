'''For a given number of rows, print the following number pyramid pattern'''
# Take number of rows as input
n = int(input("Enter the number of rows:"))

# Loop through each row
for i in range(1, n + 1):
    k = 1  # Initialize starting number for each row
    # Print numbers in the current row
    for _ in range(i):
        print(k, end=' ')
        k = k + 1  # Increment number
    print()  # Move to the next line after each row
