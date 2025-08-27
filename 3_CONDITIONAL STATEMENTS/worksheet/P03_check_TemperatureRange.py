'''Enter a temperature and print "Overheat" (>75°C), "Normal" (25-75°C), or "Low Temp" (<25°C).
Input: 18
Output: Low Temp'''
# Take temperature input from user (float value)
temp = float(input("Enter the temperature value: "))

# Check if the temperature is greater than 75
if temp > 75:
    print("overheat")   

# Check if the temperature is less than 25
elif temp < 25:
    print("Low temp")  

# If temperature is between 25 and 75
else:
    print("Normal")    
