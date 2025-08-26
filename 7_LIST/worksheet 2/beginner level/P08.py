'''Task: Write a Python program to check if a list is empty or not.
Sample input: []
Output: List is empty'''
import ast
def check_empty(lst):
    if not lst:
        print("List is empty")
    else:
        print("List is not empty")

sample_list = input("Enter list to check if it is empty or not:")
sample_list=ast.literal_eval(sample_list)
check_empty(sample_list)
