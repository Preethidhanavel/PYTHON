#Is it possible to store a function in a variable? Demonstrate how and why you might do this.
def greet():
    return "Hello!"       # Define a function that returns a greeting

say_hello = greet        # Store the function object in a variable
                         # Note: no parentheses -> we are assigning the function itself

print(say_hello())       # Call the function using the new variable -> prints "Hello!"

