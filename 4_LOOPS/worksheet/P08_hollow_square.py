'''Print a hollow square pattern of size n (n ≥ 3).'''
# Take input for the size of the square
n = int(input("Enter the size of the square (n ≥ 3): "))

# Loop through each row
for i in range(n):
    if i == 0 or i == n - 1:
        # Print the first and last row 
        print('*' * n)  
    else:
        # Print middle rows 
        print('*' + ' ' * (n - 2) + '*') 

