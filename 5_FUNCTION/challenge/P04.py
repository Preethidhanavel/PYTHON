'''Write a recursive function flatten_dict(d, p='', s='_') that takes a nested dictionary and flattens it, 
so that the result is a single-level dictionary with keys as the path joined by s.'''
import ast
def flatten_dict(d, p='', s='_'):
    flat_dict = {}
    for key, value in d.items():
        n = f"{p}{s}{key}" if p else key
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value, n, s))
        else:
            flat_dict[n] = value
    return flat_dict

n = input("Enter a nested dictionary (e.g., {'a': 1, 'b': {'c': 2}}): ")
d = ast.literal_eval(n)
print("Your nested dictionary:", d)
d1=flatten_dict(d)
print(d1)