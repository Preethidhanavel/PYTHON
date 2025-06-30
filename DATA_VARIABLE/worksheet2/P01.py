#Given the assignment a = b = 10, what happens if you later set b = 20? What is the value of a? Explain why
a=b=10
print(a,b)
b=20
print(a,b)
#here a and b points to same object. so, when we assign b to different value it'll point to different object.