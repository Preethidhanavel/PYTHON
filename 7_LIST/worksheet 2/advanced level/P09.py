'''Task: Write a Python function to find the longest common subsequence between two lists.
Sample input: [1, 3, 4, 1, 2, 3, 4, 1], [3, 4, 1, 2, 1, 3]
Output: [3, 4, 1, 3]'''
def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
   
    dp = [[[] for _ in range(n + 1)] for _ in range(m + 1)]
    
    
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i + 1][j + 1] = dp[i][j] + [X[i]]
            else:
             
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], key=len)
    
    return dp[m][n]


list1 = [1, 3, 4, 1, 2, 3, 4, 1]
list2 = [3, 4, 1, 2, 1, 3]


result = longest_common_subsequence(list1, list2)
print("Longest Common Subsequence:", result)
