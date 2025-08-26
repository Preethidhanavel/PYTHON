'''Question: Write a function multiply(x, y) that returns the product of its two arguments'''
def multiply(x:int,y:int)->int:
    return x*y
n=int(input("Enter the num1: "))
m=int(input("Enter the num2: "))
print("The product is: ",multiply(n,m))