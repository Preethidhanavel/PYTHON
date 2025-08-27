'''If a sensor value is outside the range 100–900, print "Sensor Fault". If within, print "Sensor OK".
Input: 950
Output: Sensor Fault'''
# Take input from user for sensor value (float type)
sensor_value = float(input("Enter the sensor value: "))

# Check if sensor value is within normal operating range (100 to 900)
if (sensor_value >= 100) and (sensor_value <= 900):
    print("Sensor Ok")       # Value is within range
else:
    print("Sensor Fault")    # Value is outside the normal range
