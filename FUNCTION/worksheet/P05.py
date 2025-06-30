''' Write a function is_negative(number) that returns True if the number is negative, else False.'''
def is_negative(number):
    return "True" if number<0 else "False" 
n=int(input("Enter the number: "))
print(is_negative(n))