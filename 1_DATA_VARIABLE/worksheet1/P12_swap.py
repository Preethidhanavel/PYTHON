#Swap two variable values in one line and print the values before and after swapping.
x = int(input("Enter the num1: "))  # Take first integer input
y = int(input("Enter the num2: "))  # Take second integer input

x, y = y, x  # Swap the values of x and y

print(x, y)  # Print the swapped values
