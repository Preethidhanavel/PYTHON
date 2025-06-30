#When would you use the None data type? Give an example of a good use case.
def find_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None 

print(find_even([1, 3, 5]))  
