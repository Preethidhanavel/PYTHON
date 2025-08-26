#Does Python automatically convert between integer and float types? Show a code example and explain what happens.
x = 5            # Integer value
y = 2.0          # Float value

result = x + y   # Adding int + float → result will be float (type promotion)
print(result)    # Output: 7.0

print(type(result))  # Shows the data type of result → <class 'float'>
 
