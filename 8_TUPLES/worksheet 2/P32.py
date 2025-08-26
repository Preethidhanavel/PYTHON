'''Description: Calculate the product by multiplying all the numbers in a tuple.
This is useful for aggregate calculations and is commonly found in mathematical programming and statistics.
Input: t = (4, 3, 2, 2, -1, 18)
Output: -864'''

import ast
import math
t1=input("Enter the tuple:")
t1=ast.literal_eval(t1)
print(math.prod(t1))
p=1
for i in t1:
    p*=i
print(p)