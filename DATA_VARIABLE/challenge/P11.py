#Explain the concept of interning in Python strings and its effect on variable comparison.
a = "python"
b = "python"
print(a is b)  # True -> Interned

x = "".join(["py", "thon"])
print(a == x)  # True -> Values equal
print(a is x)  # False -> Different objects in memory
