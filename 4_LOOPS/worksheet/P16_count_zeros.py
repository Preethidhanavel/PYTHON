'''Input an integer and count how many times 0 appears in it (no strings or lists).'''
# Take input from the user
n = int(input("Enter an integer: "))

# Check if the number is negative
negative = n < 0
n = abs(n)

# Initialize counter for zeros
c = 0

print("Reversed digits:")

# Loop through each digit of the number
while n > 0:
    digit = n % 10        
    if digit == 0:       
        c += 1         
    n = n // 10         

# Print the count of zeros
print(c)
