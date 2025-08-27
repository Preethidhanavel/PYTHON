'''Write a function grade(score) that returns 'A' if score ≥ 90, 'B' if 80 ≤ score < 90, 'C' if 70 ≤ score < 80, 
and 'F' for anything less.'''

# Function to determine grade based on score
def grade(score):
    if score >= 90:
        res = 'A'           # Score 90 or above gets grade A
    elif 80 <= score < 90:
        res = 'B'           # Score between 80 and 89 gets grade B
    elif 70 <= score < 80:
        res = 'C'           # Score between 70 and 79 gets grade C
    else:
        res = 'F'           # Score below 70 gets grade F
    return res

# Take input from user
n = int(input("Enter the score: "))

# Call the function and print the grade
print(grade(n))
