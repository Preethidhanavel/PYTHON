#Use augmented assignment (+=, -=, *=, /=) on a variable initialized as 10, printing its value at each step.
x = int(input("enter the num: "))  # Take integer input from user

x += x    # Add x to itself (equivalent to x = x + x)
print(x)  # Print the result

x -= x    # Subtract x from itself (equivalent to x = x - x, result will be 0)
print(x)  # Print the result

x = 10    # Assign 10 to x
x *= x    # Multiply x by itself (equivalent to x = x * x)
print(x)  # Print the result

x /= x    # Divide x by itself (equivalent to x = x / x, result will be 1.0)
print(x)  # Print the result


