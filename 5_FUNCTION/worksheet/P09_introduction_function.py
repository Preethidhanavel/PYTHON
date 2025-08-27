''' Write a function introduction(name, country='India') that prints a message introducing the person and their country.'''
# Function to print introduction, default country is India
def introduction(name, country='India'):
    print(f'"Hi I am {name} and I am coming from {country}"')

# Input person's name
n = input("Enter the name of person: ")

# Ask if person belongs to a country other than India
y = input("Does the person belong to any other country than India yes/no: ")

if y.lower() == 'yes':
    # If yes, input country name and call function
    n1 = input("Enter the country name of person: ")
    introduction(n, n1)
else:
    # Otherwise, call function with default country
    introduction(n)
