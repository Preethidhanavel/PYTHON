'''Task: Write a Python function to find the maximum sum sub-sequence in a list (sub-sequence, not necessarily contiguous).
Sample input: [2, -1, 2, 3, 4, -5]
Output: 11
(The maximum sum subsequence is 2 + 2 + 3 + 4)'''
def max_sum_subsequence(arr):
    max_sum = sum(x for x in arr if x > 0)
    return max_sum if max_sum > 0 else max(arr)  


input_list = [2, -1, 2, 3, 4, -5]

print("Maximum sum subsequence:", max_sum_subsequence(input_list))
