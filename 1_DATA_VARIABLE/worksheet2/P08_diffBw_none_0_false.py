#what is the difference between None, 0, False, and "" in Python? Are they the same or different as variables? 
#How does Python treat them in conditional statements?
if None:                             # None is treated as False in condition
    print("None is True")
else:
    print("None is False")           # Output: None is False

if 0:                                # 0 is treated as False in condition
    print("0 is True")
else:
    print("0 is False")              # Output: 0 is False

if False:                            # False is already False
    print("False is True")
else:
    print("False is False")          # Output: False is False

if "":                               # Empty string "" is also False
    print("Empty string is True")
else:
    print("Empty string is False")   # Output: Empty string is False

