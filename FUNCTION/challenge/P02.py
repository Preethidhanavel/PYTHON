''' Write a function find_duplicates(lst) that returns a list of all elements that appear more than once in the input list. 
The result should contain no duplicates and preserve the order of their first appearance.'''
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    result = []

    for item in lst:
        if item in seen:
            if item not in duplicates:
                result.append(item)
                duplicates.add(item)
        else:
            seen.add(item)

    return result

a=input("Enter the list separaeted by spaces:")
l=list(map(int,a.split()))
print(l)
x=find_duplicates(l)
print(x)
