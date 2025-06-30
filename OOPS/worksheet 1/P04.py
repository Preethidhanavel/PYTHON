'''Shape Shifters: Mastering Class Inheritance
Scenario:
Imagine you’re building a drawing tool. You have a general Shape, but want to specialize it into Circle and Square.
What you’ll learn:
The basics of inheritance
How subclasses can extend or override parent class functionality
Task:
Log Session a Shape class with a method called draw(). Inherit and customize in Circle and Square.
Example:
If you create a Circle and ask it to draw():
Expected Output:Drawing a circle'''

class Shape:
    def draw():
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

s1 = Circle()
s2 = Square()
s1.draw()
s2.draw()
