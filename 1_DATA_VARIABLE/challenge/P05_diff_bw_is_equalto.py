#Describe the difference between is and == when comparing variables. Provide an example where they behave differently.
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True → values inside lists are same
print(a is b)   # False → different list objects in memory

x = 10
y = 10
print(x is y)   # True → small integers are cached, both point to same object

s1 = "hello"
s2 = "hello"
print(s1 is s2) # True → strings with same value are stored (interned) in same memory


