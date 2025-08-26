#Why might this print False?
x = int("1000")      # Convert string "1000" to integer → x = 1000
y = int("1000")      # Convert string "1000" to integer → y = 1000

print(x is y)        # "is" checks if both variables refer to the SAME object in memory
                     # For large integers like 1000, Python usually creates separate objects
                     # So result is False (x and y are equal in value but not the same object)
