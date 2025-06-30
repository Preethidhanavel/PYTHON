'''Input an integer and count how many times 0 appears in it (no strings or lists).'''
n = int(input("Enter an integer: "))
negative = n < 0
n = abs(n)
c=0
print("Reversed digits:")
while n > 0:
    digit = n % 10        
    if digit==0:
        c+=1
    n = n // 10         

print(c)