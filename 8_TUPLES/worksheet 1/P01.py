'''Description: Log Session a tuple containing elements of various data types, including int, float, string, and bool.
This helps understand how tuples can store heterogeneous data and is useful for practical Python applications.
Input: No input; directly define the tuple.
Output: (10, 3.14, "Python", True)'''
import ast
t=input("Enter the tuple contatining different datatype items:")
t=ast.literal_eval(t)
print(t)
t=(10,3.14,'python',True)
print(t)