'''1. Crafting Your First Python Object: The Power of Instance Attributes
Scenario:
Imagine you're building a digital notebook. You want each note to have its own title and content.
What you’ll learn:
How to define classes and create objects with unique data
The magic of instance attributes in organizing information
Task:
Design a Note class with title and content as instance attributes.
Log Session two different note objects and print their details.
Example:
Suppose you create notes like “Meeting Notes” and “Grocery List”.
Output:Meeting Notes : Discuss project status with team.
Grocery List : Eggs, Milk, Bread'''

class digital_note:
    def __init__(self,title,content):
        self.title=title
        self.content=content
    def print_note(self):
        print(f"{self.title} -- {self.content}")

note1_title=input("Enter the note1 title:")
note1_content=input("Enter the note1 content:")
note2_title=input("Enter the note2 title:")
note2_content=input("Enter the note2 content:")
ob1=digital_note(note1_title,note1_content)
ob1.print_note()

ob2=digital_note(note2_title,note2_content)
ob2.print_note()

print("note1")
print(f"{ob1.title}-->{ob1.content}")
print("note2")
print(f"{ob2.title}-->{ob2.content}")