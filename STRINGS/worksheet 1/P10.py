'''Generate Random Strings Until a Target String is Formed
Explanation: Keep generating random strings until you produce the target string.
Input: Target = "abc"
Expected Output: Randomly generated 'abc' after N attempts (N will vary)'''
import string
import random

allchar=string.ascii_lowercase+string.ascii_uppercase+string.digits+' ., !?;:'
def generate_random_string(l):
    return ''.join(random.choice(allchar) for _ in range(l))

def fitness_check(s):
    return sum(1 for i,j in zip(s,t) if i==j )

def mutate(s):
    i=random.randint(0,len(s)-1)
    l=list(s)
    l[i]=random.choice(allchar)
    return ''.join(l)


t=input("Enter the target string:")
match=generate_random_string(len(t))
iteration=0

while match!=t:
    print(match)
    mutated=mutate(match)
    if fitness_check(mutated)>=fitness_check(match):
        match=mutated

    iteration+=1

print(iteration,match,mutated)
