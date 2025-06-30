'''Write a function greet_person(name, greeting) that prints a personalized message like "Hello, John!" using the arguments.'''
def greet_person(name,greeting):
    print(f'"{greeting},{name}!"')

n=input("Enter the name of person: ")
g=input("Enter the greeting: ")
greet_person(n,g)