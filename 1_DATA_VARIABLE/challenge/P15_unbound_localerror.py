#How are global and local variables managed in Python functions? Provide an example that demonstrates a
#UnboundLocalError
x = 10   # Global variable

def example():
    print(x)   #  Error: Python thinks 'x' is local because we assign to it below
    x = 5      # Local variable (assignment makes 'x' local inside this function)

example()
