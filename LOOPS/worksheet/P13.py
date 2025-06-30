'''Print the sum of all odd numbers from 1 up to n (inclusive), using loops only.'''
n=int(input("Enter the number range n:"))
sum=0
for i in range(1,n+1,2):
    sum+=i
print("Sum of odd numbers : ",sum)
