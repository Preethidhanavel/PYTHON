'''Task: Write a Python program to get a list, 
sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample input: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''
def sort_by_last_element(tuples_list):
    # Use the sorted() function with a key that returns the last element of each tuple
    return sorted(tuples_list, key=lambda x: x[-1])

tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_tuples = sort_by_last_element(tuples)
print("Sorted list:", sorted_tuples)
