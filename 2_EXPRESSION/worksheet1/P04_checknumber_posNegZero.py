#Check if a Number is Positive, Negative, or Zero (Conditional Expression)
#Use a single line expression to print whether a number is positive, negative, or zero.
#Sample Input: num = -8
# Take input from the user
num = int(input("Enter the num: "))

# Check whether the number is positive, negative, or zero
print("Positive" if (num > 0) else "Negative" if (num < 0) else "zero")
