'''Write a function greet_person(name, greeting) that prints a personalized message like "Hello, John!" using the arguments.'''
# Function to greet a person with a custom greeting
def greet_person(name, greeting):
    print(f'"{greeting}, {name}!"')

# Take name input from user
n = input("Enter the name of person: ")

# Take greeting input from user
g = input("Enter the greeting: ")

# Call the function to greet the person
greet_person(n, g)
