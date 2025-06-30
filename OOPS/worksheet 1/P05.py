''' One for All: The Magic of Class Attributes
Scenario:
All students in a school belong to the same institution. How can you ensure this is reflected in every student object?
What you’ll learn:
Class (static) attributes: properties shared by all instances
When and why to use them
Task:
Define a Student class where every student has the same school_name.
Example:
If you create two students and print their school_name:
Expected Output:Central High School Central High School'''

class Student:
    school_name = "Central High School" 

    def __init__(self, name):
        self.name = name 
    def print_detail(self):
        print(f"{self.name} studing in {self.school_name}")


name1=input("Enter the student name 1:")
name2=input("Enter the student name 2:")
s1 = Student(name1)
s2 = Student(name2)

s1.print_detail()
s2.print_detail()
