''' Write a function is_negative(number) that returns True if the number is negative, else False.'''
# Function to check if a number is negative
def is_negative(number):
    return "True" if number < 0 else "False"  # Return True if number < 0, else False

# Take input from user
n = int(input("Enter the number: "))

# Call the function and print the result
print(is_negative(n))
