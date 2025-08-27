'''Accept a device mode value:
- 0: "Standby"
- 1: "Active"
- 2: "Fault"
- Any other: "Unknown mode"'''
# Read the device module value (0, 1, 2, or other)
v = int(input("Enter the device module value: "))

# Check the device mode based on input value
if v == 0:
    print("standby")      
elif v == 1:
    print("Active")      
elif v == 2:
    print("Fault")       
else:
    print("unknown mode") 
