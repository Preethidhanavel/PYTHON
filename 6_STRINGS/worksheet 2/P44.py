'''Split String into Groups of n Characters
Explanation: Divide a string into equal-sized chunks.
Input: "abcdefgh", n = 3
Expected Output: ['abc', 'def', 'gh']'''
def split_into_chunks(s, n):
    l=[]
    for i in range(0, len(s), n):
        l.append(s[i:i+n]) 
    return l


s = input("Enter the string: ")
n = int(input("Enter the chunk size: "))
result = split_into_chunks(s, n)
print("Chunks:", result)
