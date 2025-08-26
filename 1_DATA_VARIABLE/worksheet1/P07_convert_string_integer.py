#Convert a numeric string ("50") to an integer and a float,
#then print the converted values and their types.
s = str(input("Enter the string: "))  # Take string input from user

print("Before conversion ", s)         # Print the original string

x = int(s)    # Convert string to integer
y = float(s)  # Convert string to float

print("After conversion", x, y)       # Print the converted integer and float values
