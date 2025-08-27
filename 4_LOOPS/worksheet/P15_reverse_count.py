'''Print all numbers from n down to 1 using a single loop.'''
# Take input from the user
n = int(input("Enter the number: "))

# Print numbers from n down to 1
for i in range(n, 0, -1):
    print(i, end="  ")
