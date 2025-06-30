'''Frequency of Consecutive Characters
Explanation: Count how many times each character repeats in sequence.
Input: "aabccddd"
Expected Output: {'a': 2, 'b': 1, 'c': 2, 'd': 3}'''
def count_freq(s):
	f={}
	for i in s:
		f[i]=f.get(i,0)+1
	print(f)
s=input("Enter the string:")
count_freq(s)