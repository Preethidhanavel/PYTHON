#When would you use the None data type? Give an example of a good use case.
def find_even(numbers):
    # Loop through each number in the list
    for num in numbers:
        if num % 2 == 0:    # Check if the number is even
            return num       # Return the first even number found
    return None              # If no even number is found, return None

print(find_even([1, 3, 5]))  # List has no even numbers → prints None

