#What will be the output and the type of each variable?
x = 2          # integer value
y = 2.0        # float value
z = "2"        # string value

w = x + int(z) # convert string "2" to int and add with x → 2 + 2 = 4
v = str(x) + z # convert x (2) to string and concatenate with "2" → "22"

print(w)       # prints 4
print(v)       # prints "22"
