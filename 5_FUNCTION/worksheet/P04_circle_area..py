''' Write a function area_of_circle(radius) that returns the area (πr²) of a circle for the given radius'''
# Function to calculate the area of a circle
def area_of_circle(radius):
    pi = 22/7                  # Approximate value of pi
    return pi * (radius ** 2)  # Area = π * r^2

# Take radius input from user
r = float(input("Enter the radius: "))

# Call the function and print the area
print(area_of_circle(r))
