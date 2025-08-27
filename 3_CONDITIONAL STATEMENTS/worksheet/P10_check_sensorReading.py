'''Given three sensor readings, print "Majority High" if at least two readings are above a threshold (e.g., 50), 
otherwise "Majority Low".
Input: 40, 65, 70
Output: Majority High'''
# Take input readings from three sensors
s1 = int(input("Enter the sensor 1 reading: "))
s2 = int(input("Enter the sensor 2 reading: "))
s3 = int(input("Enter the sensor 3 reading: "))

# Check if the majority of sensors have readings above 50
if (s1 > 50 and s2 > 50) or (s2 > 50 and s3 > 50) or (s1 > 50 and s3 > 50):
    print("Majority High")   # At least two sensors have high readings
else:
    print("Majority Low")    # Less than two sensors have high readings
