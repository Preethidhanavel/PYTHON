#Assign an integer to a variable, then reassign it to a float and string sequentially, printing type and value after each step.
x=int(input("Enter the num: "))
print("x=",x,"type=",type(x))
x=float(x)
print("x=",x,"type=",type(x))
x=str(x)
print("x=",x,"type=",type(x))