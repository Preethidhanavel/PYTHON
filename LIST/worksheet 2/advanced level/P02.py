'''Task: Write a Python function to find the length of the longest increasing sub-sequence in a list of numbers.
Sample input: [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: 6
(The longest increasing subsequence is [10, 22, 33, 50, 60, 80])'''
import ast
def longest_increasing_subsequence(l):
    n = len(l)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)



l=input("Enter the list :")
l=ast.literal_eval(l)


print("Length of LIS:", longest_increasing_subsequence(l))
