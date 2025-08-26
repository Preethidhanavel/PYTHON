#Slice the string "PythonProgramming" into "Python" and "Programming" separately and print both results.
x = "Pythonprogramming"   # Assign a string to x

t1 = x[:6]    # Slice the first 6 characters from index 0 to 5
t2 = x[6:]    # Slice from index 6 to the end of the string

print(t1)     # Print first part of the string ("Python")
print(t2)     # Print second part of the string ("programming")
