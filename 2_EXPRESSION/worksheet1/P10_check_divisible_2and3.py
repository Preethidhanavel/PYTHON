#Check if a Number is Divisible by Both 2 and 3
#Write a single expression that evaluates to True if a number is divisible by both 2 and 3, otherwise False.
#Sample Input: num = 18
# Take a number as input
num = int(input("Enter the num: "))

# Check if the number is divisible by both 2 and 3
x = (num % 2 == 0) and (num % 3 == 0)

# Print result
print("True" if (x) else "False")
