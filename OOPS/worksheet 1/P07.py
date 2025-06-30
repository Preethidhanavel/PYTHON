''' Are You One of Us? Checking Class Membership
Scenario:
You want to make sure a Bus object can access special parking. But only if it’s really a Vehicle.
What you’ll learn:
Using isinstance() to check an object’s class or parent classes
Dynamic type safety
Task:
Check if a Bus object is an instance of Vehicle.
Example:
You check with isinstance() for a Bus object.
Expected Output:True'''

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bus(Vehicle):
    def park(self):
        print("Bus is parking")

class Car:
    def status(self):
        print("Car parked!")

b = Bus()
print(isinstance(b, Vehicle))
c=Car()
print(isinstance(c,Vehicle))