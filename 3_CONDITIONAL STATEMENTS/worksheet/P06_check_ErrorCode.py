'''Take an error code (integer). Print "Critical" if code ≥1000, "Warning" if 100–999, and "Info" if <100.
Input: 230
Output: Warning'''
# Take input from user for error code (integer)
code = int(input("Enter error code: "))

# Check if code indicates a critical error 
if code >= 1000:
    print("Critical")      

# Check if code indicates a warning 
elif (100 <= code <= 999):
    print("Warning")       

# Otherwise, it is informational 
else:
    print("Info")          

