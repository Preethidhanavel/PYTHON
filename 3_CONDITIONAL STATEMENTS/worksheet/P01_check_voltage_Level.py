'''Given a voltage reading, print "Under Voltage", "Nominal", or "Over Voltage".
(Nominal is between 3.0V and 3.3V inclusive.)
Input: 3.35
Output: Over Voltage'''
# Take voltage input from user 
n = float(input("Enter the voltage: "))

# Check if voltage is greater than 3.3 
if n > 3.3:
    print("Overvoltage")

# Check if voltage is less than 3.0 
elif n < 3.0:
    print("Undervoltage")

# If voltage is between 3.0 and 3.3 (inclusive)
else:
    print("Nominal voltage")

