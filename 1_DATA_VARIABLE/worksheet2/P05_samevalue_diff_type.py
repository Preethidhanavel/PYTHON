#How does Python treat variable names that have the same value 
# but are of different data types?
#For example, what is the result of 3 == 3.0 and 3 is 3.0?
x = 3             # x is an integer 
y = float(3.0)    # y is a floating-point number 

print(x == y)     # compares int (3) and float (3.0)
                  # Result is True because values are equal, even if types differ
