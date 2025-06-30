'''Family Traits: Inheritance in Action with Vehicles and Buses
Scenario:
You’re modeling a transportation system. Buses are vehicles, so shouldn’t they share common features?
What you’ll learn:
Inheriting attributes and methods from a parent class
The principle of code reuse and extension
Task:
Log Session a Vehicle class and a Bus class that inherits from it. Demonstrate shared behavior.
Example:
Suppose you make a Bus object and call its move() method. 
Expected Output:Vehicle is moving'''

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h")


class Bus(Vehicle):
    def __init__(self, brand, speed, route_number):
        super().__init__(brand, speed)
        self.route_number = route_number

    def display_route(self):
        print(f"Bus is on route number {self.route_number},{self.brand}")

name=input("Enter the bus name:")
speed=int(input("enter the speed of bus:"))
route_number=int(input("Enter the route_number"))
city_bus = Bus(name,speed,route_number)


city_bus.move()           
city_bus.display_route()   
