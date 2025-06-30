#How does variable assignment differ between mutable and immutable objects? 
#Illustrate with an example.
#Mutable objects: both variables can reference the same object, and changes affect both.
#Immutable objects: assignment creates a new object on modification.
x=5
y=x
print(x,y)
x=10
print(x,y)
a=[1,2,3]
b=a
print(a,b)
a[0]=9
print(a,b)