#What is the significance of the id() function when working with variables of immutable and mutable types?
x = 100
print(id(x))   # Print the memory address of integer object 100

x += 1         # x = x + 1 -> integers are immutable, so a NEW object (101) is created
print(id(x))   # Different id -> because x now refers to a new integer object

a = [1, 2]
print(a, id(a))   # Print list and its memory address

a.append(3)       # Lists are mutable -> element 3 is added inside the SAME object
print(a, id(a))   # Same id -> because list is modified in place, no new object created


