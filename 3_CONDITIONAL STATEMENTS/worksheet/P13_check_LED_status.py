'''Given the status of three LEDs (on/off as 1/0), print which LEDs are ON. If all are off, print "All LEDs off".
Input: 0, 1, 0
Output: LED2 ON'''

# Read the status of three LEDs (0 = OFF, 1 = ON)
led1 = int(input("Enter status of LED1 (0/1): "))
led2 = int(input("Enter status of LED2 (0/1): "))
led3 = int(input("Enter status of LED3 (0/1): "))

# Check and print which LEDs are ON
if led1:
   print("LED1 ON")  
if led2:
   print("LED2 ON")  
if led3:
   print("LED3 ON")  

# If all LEDs are OFF, print message
if (not led1) and (not led2) and (not led3):
   print("All LEDs off")   # No LED is ON

