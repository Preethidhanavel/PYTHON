''' Write a function area_of_circle(radius) that returns the area (πr²) of a circle for the given radius'''
def area_of_circle(radius):
    pi=22/7
    return pi*(radius**2)
r=float(input("Enter the radius: "))
print(area_of_circle(r))