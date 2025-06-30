'''9. Polymorphism in the Real World: Area of Shapes
Scenario:
You’re making a geometry tool. Different shapes need to compute area, but each does it differently.
What you’ll learn:
Polymorphism: different classes, same interface
Practical OOP design patterns
Task:
Log Session a Shape base class with an area() method, then implement it differently in Circle and Square.
Example:
If you create a Square with side 4 and call area():
Expected Output:16'''

import math

class Shape():
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

r=int(input("Enter the radius of circle:"))
l=int(input("Enter the length of square:"))
s = Square(l)
c = Circle(r)
k=Shape()
print(s.area()) 
print(round(c.area(), 2)) 
