#Store two float numbers, add them, and print the result rounded to two decimal places.

x=float(input("Enter the num:"))
y=float(input("Enter the num2:"))
z=x+y #sum of two float numbers  
print(round(z,2))#rounded to 2 decimal place
print("%.2f"%z)
print(f"{z:.2f}")
