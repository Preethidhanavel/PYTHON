'''Convert Integer to String and Vice Versa
Explanation: Change a number to a string, and a string of digits to an integer.
Input: Integer = 123, String = "456"
Expected Output:
Integer to string: '123'
String to integer: 456'''
s=input("Enter the string of digits:")
n=int(input("Enter the integer:"))
print("string to int:",int(s))
print("integer to string:",f"'{str(n)}'")
sum=0
for i in s:
    sum=sum*10+int(i)

print(sum)
w=''
while n!=0:
    r=n%10
    w=str(r)+w
    n//=10

print(w)