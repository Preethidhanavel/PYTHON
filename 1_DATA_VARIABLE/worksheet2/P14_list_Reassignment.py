#What is the value of y and why?
x = [1, 2, 3]   # x points to a list [1, 2, 3]
y = x           # y refers to the same list as x
x = [4, 5, 6]   # x is reassigned to a new list, y still points to old list
print(y)        # y still shows [1, 2, 3]
