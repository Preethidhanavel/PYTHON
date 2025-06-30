#Swap Two Numbers Without Using a Third Variable
#Swap two variables’ values using a single line of code.
#Sample Input: a = 15, b = 8
a=int(input("Enter the a: "))
b=int(input("Enter the b: "))
print("Befor swapping ",a,b)
a,b=b,a
print("After swapping ",a,b)