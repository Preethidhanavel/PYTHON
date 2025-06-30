#What is the significance of the id() function when working with variables of immutable and mutable types?
x=100
print(id(x))
x+=1
print(id(x))
a=[1,2]
print(a,id(a))
a.append(3)
print(a,id(a))

