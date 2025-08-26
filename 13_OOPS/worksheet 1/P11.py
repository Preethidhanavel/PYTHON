'''11. Meet the Person: Calculate Age from Date of Birth
Scenario:
Log Session a birthday tracker! Determine someone’s age from their date of birth.
What you’ll learn:
Handling dates and calculating with them
Real-world use of classes
Task:
Make a Person class and compute age.
Example:
For a person born on 2000-05-25 (today is 2025-05-25):
Expected Output:Alice is 25 years old.'''

from datetime import datetime, date

class Person:
    def __init__(self, name, dob_str):
        self.name = name
        self.dob = datetime.strptime(dob_str, "%Y-%m-%d").date()

    def calculate_age(self):
        today = date.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age

    def show_age(self):
        print(f"{self.name} is {self.calculate_age()} years old.")
        
name=input("Enter the name:")
dob=input("Enter the date of birth:")

p = Person(name,dob)
p.show_age()
