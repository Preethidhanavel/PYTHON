#Assign an integer to a variable, then reassign it to a float and string sequentially, printing type and value after each step.
x = int(input("Enter the num: "))  # Take integer input from user
print("x=", x, "type=", type(x))   # Print value and type of x (int)

x = float(x)  # Convert integer x to float
print("x=", x, "type=", type(x))   # Print value and type of x (float)

x = str(x)    # Convert float x to string
print("x=", x, "type=", type(x))   # Print value and type of x (str)
