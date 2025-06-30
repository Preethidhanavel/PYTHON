'''Print all 4-digit numbers where the product of the first two digits equals the product of the last two digits.
Valid Example: 1441 → (1 × 4) == (4 × 1) → 4 == 4 (valid)
Invalid Example: 2356 → (2 × 3) == (5 × 6) → 6 == 30 (not valid)'''
for num in range(1000, 10000):
    a = num // 1000           
    b = (num // 100) % 10      
    c = (num // 10) % 10        
    d = num % 10                

    if a * b == c * d:
        print(num,end=" ")
