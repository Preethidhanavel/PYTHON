#Find the Difference Between the Largest and Smallest of Three Numbers (Using Only Expressions)
#Write an expression to find the difference between the largest and the smallest of three numbers.
#Sample Input: a = 8, b = 27, c = 14
# Take three integer inputs from the user
a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
c = int(input("Enter the c: "))

# Find the largest number among a, b, c
x = a if a > b and a > c else b if b > c else c

# Find the smallest number among a, b, c
y = a if a < b and a < c else b if b < c else c

# Print the absolute difference between the largest and smallest
print(abs(x - y))
