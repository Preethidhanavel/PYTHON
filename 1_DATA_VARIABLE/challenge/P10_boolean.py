#How does Python treat Boolean values as integers? Show an example where this is useful.
lst = [5, 10]          # list with two elements
index = (3 > 7)        # condition -> False (because 3 is not greater than 7)
print(lst[index])      # lst[False] -> lst[0] -> 5

data = {True: "yes", False: "no"}   # dictionary with boolean keys
print(data[1])         # 1 == True -> prints "yes"
print(data[0])         # 0 == False -> prints "no"
  
