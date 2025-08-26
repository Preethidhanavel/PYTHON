#Rotate Bits Left by k Positions
#Given a number (assume 8 bits) and a value k, write an expression to rotate its bits to the left by k positions.
#Sample Input: n = 150, k = 2
n=int(input("Enter the number: "))
k=int(input("Enter the number of rotation: "))
k=k%32
x=(n << k) | (n >> (32 - k))
print(bin(n))
print(bin(x)," ",x)