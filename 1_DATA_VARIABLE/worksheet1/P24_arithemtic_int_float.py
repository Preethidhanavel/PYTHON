#Perform arithmetic between integer (10) and float (3.5) variables, then print the result and its type.
x = int(input("Enter int value: "))     # Take integer input from user
y = float(input("Enter the float value: "))  # Take float input from user

print(x + y)       # Print sum of x and y
print(x - y)       # Print difference of x and y
print(x * y)       # Print product of x and y
print(round(x / y, 3))  # Print division of x by y rounded to 3 decimal places
print(x // y)      # Print integer division (quotient) of x divided by y
print(x % y)       # Print remainder of x divided by y
