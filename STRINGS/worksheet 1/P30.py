'''Count Frequency of Words in String (Short Form)
Explanation: Show how many times each word appears.
Input: "apple apple orange"
Expected Output: {'apple': 2, 'orange': 1}'''
def count_word(s):
    s=s.split()
    f={}
    for i in s:
        f[i]=f.get(i,0)+1
    print(f)
s=input("Enter the string:")
count_word(s)