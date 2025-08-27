#Swap Two Numbers Without Using a Third Variable
#Swap two variables’ values using a single line of code.
#Sample Input: a = 15, b = 8
# Take first number as input
a = int(input("Enter the a: "))

# Take second number as input
b = int(input("Enter the b: "))

# Print values before swapping
print("Before swapping ", a, b)

# Swap the values of a and b 
a, b = b, a

# Print values after swapping
print("After swapping ", a, b)
