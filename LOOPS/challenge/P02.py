'''For n between 100 and 999, print all numbers where the sum of their digits raised to their own position is equal to the number.
Valid Example: 135: 1¹ + 3² + 5³ = 1 + 9 + 125 = 135 (valid)
Invalid Example: 123: 1¹ + 2² + 3³ = 1 + 4 + 27 = 32 (not valid)'''
for i in range(100,1000):
    a=i//100
    b=(i//10)%10
    c=i%10
    sum=(a**1)+(b**2)+(c**3)
    if(sum==i):
        print(i,end=" ")