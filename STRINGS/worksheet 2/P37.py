'''Generate a Random Binary String
Explanation: Log Session a string of a given length containing only random 0s and 1s.
Input: Length = 8
Expected Output: e.g., "10101001"'''

import random
def rand_key(p):
    key1 = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key1 += temp
        
    return(key1)


n = int(input("Enter the length:"))
str1 = rand_key(n)
print("Desired length random binary string is: ", str1)