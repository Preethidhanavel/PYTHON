''' The Ultimate Calculator: Basic Arithmetic by OOP
Scenario:
Build your own pocket calculator with class-based design.
What you’ll learn:
Encapsulating operations in methods
Using OOP for real utilities
Task:
Log Session a Calculator class with methods for add, subtract, multiply, and divide.
Example:
Adding 4 and 5, then dividing 10 by 2: 
Expected Output:9
5.0'''

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b


calc = Calculator()

print(calc.add(10, 5))        
print(calc.subtract(10, 5))   
print(calc.multiply(10, 5))   
print(calc.divide(10, 5))     
print(calc.divide(10, 0))    
