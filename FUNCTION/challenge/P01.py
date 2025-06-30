''' Write a function deep_sum(lst) that takes a nested list of integers (arbitrary levels of nesting) and 
returns the total sum of all integers.'''
import ast
def deep_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += deep_sum(item) 
    return total
n = input("Enter numbers separated by spaces and nested list: ")
l = ast.literal_eval(n)
print("List:", l)
print(f"The total of list element is {deep_sum(l)}")