'''Filter Strings with a Combination of k Substrings
Explanation: From a list, select only the strings that contain all of a set of k substrings.
Input: List = ["applebanana", "apple", "banana", "applebananacherry"], Substrings = ["apple", "banana"]
Expected Output: ["applebanana", "applebananacherry"]'''



test_list =["applebanana", "apple", "banana", "applebananacherry"]
print("The original list : " ,test_list)

substr_list = ["apple", "banana"]


res = []
for s in test_list:
    if all(sub in s for sub in substr_list):
        res.append(s)

print("Strings after joins : " ,res)