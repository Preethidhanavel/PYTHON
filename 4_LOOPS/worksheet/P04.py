'''For a given number of rows, print the following number pyramid pattern'''
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    k=1
    for _ in range(i):
        print(k,end=' ')
        k=k+1
    print()