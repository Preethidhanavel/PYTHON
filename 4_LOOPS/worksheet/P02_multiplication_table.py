'''For a given number, print its multiplication table from 1 to 10, but don’t use the * operator.'''
# Take input number from user
num = int(input("Enter a number: "))

# Loop through 1 to 10 to generate multiplication table
for i in range(1, 11):
    product = 0
    # Calculate multiplication by repeated addition
    for _ in range(i):
        product += num
    # Print the result
    print(f"{num} x {i} = {product}")

