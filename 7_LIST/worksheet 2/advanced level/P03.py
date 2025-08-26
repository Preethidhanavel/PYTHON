'''Task: Write a Python function that generates all the permutations of the elements in a given list.
Sample input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]'''

def permute(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    res = []
    for i in range(len(arr)):
        elem = arr[i]
        rem = arr[:i] + arr[i+1:]
        for p in permute(rem):
            res.append([elem] + p)
    return res

s = [1, 2, 3]
res=[]
for p in permute(s):
    res.append(list(p))
print(res)
