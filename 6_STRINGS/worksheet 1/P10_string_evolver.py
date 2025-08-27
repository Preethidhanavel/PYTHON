'''Generate Random Strings Until a Target String is Formed
Explanation: Keep generating random strings until you produce the target string.
Input: Target = "abc"
Expected Output: Randomly generated 'abc' after N attempts (N will vary)'''
import string
import random

# Define the pool of characters that can be used
allchar = string.ascii_lowercase + string.ascii_uppercase + string.digits + ' ., !?;:'

# Function to generate a random string of given length
def generate_random_string(l):
    return ''.join(random.choice(allchar) for _ in range(l))

# Function to check fitness: counts how many characters match with target
def fitness_check(s):
    return sum(1 for i, j in zip(s, t) if i == j)

# Function to mutate a string by changing one random character
def mutate(s):
    i = random.randint(0, len(s) - 1)   # Random index
    l = list(s)                         # Convert string to list for mutability
    l[i] = random.choice(allchar)       # Replace one character randomly
    return ''.join(l)                   # Return new string


# ---- Main Execution ----
t = input("Enter the target string: ")              # Target string to match
match = generate_random_string(len(t))              # Start with a random guess
iteration = 0                                       # Counter for number of iterations

# Loop until the generated string matches the target
while match != t:
    print(match)                                    # Print current string
    mutated = mutate(match)                         # Create a mutated version
    
    # Keep mutation only if fitness improves or stays the same
    if fitness_check(mutated) >= fitness_check(match):
        match = mutated
    
    iteration += 1                                  # Count iterations

# Print final results
print(iteration, match, mutated)
