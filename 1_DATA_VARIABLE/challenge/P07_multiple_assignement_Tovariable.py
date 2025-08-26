#Given the code below, what is the final value and type of x after all assignments?
x = 3          # x is an integer (3)
x += 2.0       # add 2.0 -> result is float (5.0)
x = str(x)     # convert float 5.0 to string -> "5.0"
x += '1'       # string concatenation -> "5.0" + "1" = "5.01"
print(x, type(x))  # Output: 5.01 <class 'str'>
