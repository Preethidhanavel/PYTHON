'''Given a voltage and current reading, print "Power OK" if both are in safe ranges, otherwise print specific error:
- Voltage out of 3.0–3.3V: "Voltage Error"
- Current out of 10–500mA: "Current Error"
- Both out: "Power Error"'''

# Read voltage value in volts
voltage = float(input("Enter voltage (in volts): "))

# Read current value in mA
current = int(input("Enter current (in mA): "))

# Check if voltage is within acceptable range 
voltage_ok = 3.0 <= voltage <= 3.3

# Check if current is within acceptable range 
current_ok = 10 <= current <= 500

# Decision based on voltage and current status
if voltage_ok and current_ok:
    print("Power OK")          
elif not voltage_ok and not current_ok:
    print("Power Error")     
elif not voltage_ok:
    print("Voltage Error")    
else:
    print("Current Error")     

