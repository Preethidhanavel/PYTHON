#Can you modify a string in place in Python? If not, explain why with reference to data types.
s = "hello"

# s = 'H' + s[1:]   # This works -> creates a new string "Hello"

s[0] = 'H'         #  Error ->strings are immutable, you cannot change characters in place

print(s)           # This line will not run because of the error

