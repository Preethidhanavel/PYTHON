'''Find all numbers less than 1000 which equal the sum of the factorials of their digits.
Valid Example: 145: 1! + 4! + 5! = 1 + 24 + 120 = 145 (valid)
Invalid Example: 123: 1! + 2! + 3! = 1 + 2 + 6 = 9 (not valid)'''
def fact(n):
    f=1
    for i in range(n,0,-1):
        f*=i
    return f

for i in range(1,1000):
    n=i
    sum=0
    while n!=0:
        r=n%10
        sum+=fact(r)
        n//=10
    if(sum==i):
        print(i," ")