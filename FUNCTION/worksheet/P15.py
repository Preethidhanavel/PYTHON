'''Question: Write a recursive function fibonacci(n) that returns the nth Fibonacci number'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
a=int(input("Enter the number: "))
print(f"the {a} fibonacci number is {fibonacci(a)}")