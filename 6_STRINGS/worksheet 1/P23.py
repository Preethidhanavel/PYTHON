'''Convert a String to a Set (Unique Characters)
Explanation: Keep only unique characters from the string.
Input: "balloon"
Expected Output: {'b', 'a', 'l', 'o', 'n'}'''
def str_set(s):
    seen=[]
    for i in s:
        if i not in seen:
            seen.append(i)
    return set(seen)
s=input("Enter the string:")
print(str_set(s))