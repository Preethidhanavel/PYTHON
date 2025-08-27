'''Given three boolean flags: `power_on`, `overcurrent`, `overvoltage`, print:
- "System Safe" if only `power_on` is True.
- "Shut Down: Overcurrent" if `overcurrent` is True.
- "Shut Down: Overvoltage" if `overvoltage` is True.
- "Critical Failure" if both faults are True.
Input: True, True, False
Output: Shut Down: Overcurrent'''
# Function to convert input string to boolean
def to_bool(x):
    # Returns True only if the string is exactly 'True'
    return x in ('True')

# Take input from user for different system flags
power_on    = input("Enter the status of power_on flag value: ")
overcurrent = input("Enter the status of overcurrent flag value: ")
overvoltage = input("Enter the status of overvoltage flag value: ")

# Convert string inputs to boolean values
overvoltage = to_bool(overvoltage)
overcurrent = to_bool(overcurrent)
power_on    = to_bool(power_on)

# Check system conditions and print appropriate status
if overcurrent and overvoltage:
    print("Critical Failure")         
elif overcurrent:
    print("Shut Down: Overcurrent")   
elif overvoltage:
    print("Shut Down: Overvoltage")  
elif power_on:
    print("System Safe")            
else:
    print("System Off")            

