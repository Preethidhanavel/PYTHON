#Given x = [1, 2, 3] and y = x, then x[0] = 9. What are the values of x and y? Explain the behavior.
x = [1, 2, 3]   # x is a list with elements
y = x           # y points to the same list as x (no copy made)

print(x, y)     # prints [1, 2, 3] [1, 2, 3]

x[0] = 9        # modify the first element of the list via x

print(x, y)     # both x and y show [9, 2, 3] because they reference the same list
