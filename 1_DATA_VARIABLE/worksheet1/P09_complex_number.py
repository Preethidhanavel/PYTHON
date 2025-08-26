#Assign two complex numbers, then print their sum, difference, and product.
x = str(input("Enter the complex1: "))  # Take first complex number as string
y = str(input("Enter the complex2: "))  # Take second complex number as string

x = complex(x)  # Convert string input to complex number
y = complex(y)  # Convert string input to complex number

# Print sum of real and imaginary parts separately
print("sum: real", x.real + y.real, "imaginary", x.imag + y.imag)

# Print difference of real and imaginary parts separately
print("difference: real", x.real - y.real, "imaginary", x.imag - y.imag)

print(x + y)  # Print full complex sum
print(x - y)  # Print full complex difference
print(x * y)  # Print product of two complex numbers
