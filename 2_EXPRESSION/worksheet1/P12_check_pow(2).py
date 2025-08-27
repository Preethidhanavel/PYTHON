#Check if a Number is a Power of Two
#Write a single Boolean expression to check if a number is a power of two.
#Sample Input: n = 32
# Take an integer input from the user
n = int(input("Enter the n: "))

# Check if 'n' is a power of 2
x = n > 0 and ((n & (n - 1)) == 0)

# Print Result
print("power of 2" if (x) else "false")
