#Add an integer (25) and a numeric string ("25") after converting the string explicitly, and print the result.
x = int(input("Enter the num: "))  # Take an integer input from user
y = str(input("Enter the string : "))  # Take string input from user

z = int(y)   # Convert the string input to integer

print(x + z)  # Print the sum of x and converted integer z
