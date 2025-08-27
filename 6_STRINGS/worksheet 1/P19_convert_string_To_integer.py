'''Convert Integer to String and Vice Versa
Explanation: Change a number to a string, and a string of digits to an integer.
Input: Integer = 123, String = "456"
Expected Output:
Integer to string: '123'
String to integer: 456'''
# Take a string of digits from user
s = input("Enter the string of digits: ")

# Take an integer from user
n = int(input("Enter the integer: "))

# Convert string to integer using int()
print("string to int:", int(s))

# Convert integer to string using str()
print("integer to string:", f"'{str(n)}'")

# ---- Manual string to integer conversion ----
sum = 0
for i in s:
    sum = sum * 10 + int(i)  # Build number digit by digit

print(sum)  # Print manually converted integer

# ---- Manual integer to string conversion ----
w = ''
while n != 0:
    r = n % 10          # Extract last digit
    w = str(r) + w      # Append digit at front
    n //= 10            # Remove last digit

print(w)  # Print manually converted string
