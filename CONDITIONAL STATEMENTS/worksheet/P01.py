'''Given a voltage reading, print "Under Voltage", "Nominal", or "Over Voltage".
(Nominal is between 3.0V and 3.3V inclusive.)
Input: 3.35
Output: Over Voltage'''
n=float(input("Enter the voltage: "))
if n>3.3:
    print("overvoltage")
elif n<3.0:
    print("Undervoltage")
else:
    print("Nominal voltage")
