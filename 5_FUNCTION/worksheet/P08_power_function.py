''' Write a function power(base, exponent=2) that returns base raised to exponent (default is square).'''
# Function to calculate power with default exponent as 2
def power(base, exponent=2):
    return base ** exponent

# Take base input from user
n = int(input("Enter the number: "))

# Ask user if they want to enter exponent
y = input("Do you want to enter the exponent yes/no: ")

if y.lower() == 'yes':
    # If yes, take exponent input and calculate power
    n1 = int(input("Enter the exponent: "))
    print(f'The result is {power(n, n1)}')
else:
    # If no, use default exponent 2
    print(f'The result is {power(n)}')
