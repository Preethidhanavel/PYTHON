'''Write a function sign(num) that returns 'Positive' if num > 0, 'Negative' if num < 0, and 'Zero' if num == 0'''
# Function to determine the sign of a number
def sign(num):
    return 'Zero' if num == 0 else 'Positive' if num > 0 else 'Negative'

# Take input from user
n = int(input("Enter the number: "))

# Call the function and print the sign of the number
print(f'The given number is {sign(n)}')
