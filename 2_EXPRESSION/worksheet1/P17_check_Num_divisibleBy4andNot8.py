#Check If a Number is a Multiple of 4 but Not of 8
#Write an expression that is True only if a number is divisible by 4 but not by 8.
#Sample Input: n = 12
# Take an integer input from the user
n = int(input("Enter the number: "))

#  n must be divisible by 4 and must not be divisible by 8 
x = (n % 4 == 0) and (n % 8 != 0)

# Print "True" if the condition is satisfied, otherwise print "False"
print("True" if (x) else "False")
