'''Enter two analog readings. Print "Match" if they are within 5 units of each other, "No Match" otherwise.
Input: 98, 101
Output: Match'''
# Read two analog sensor readings
a1 = int(input("Enter the analog reading 1: "))
a2 = int(input("Enter the analog reading 2: "))

# Compare the readings
if abs(a1 - a2) >= 0 and abs(a1 - a2) <= 5:
    print("Match")      # Readings are close enough
else:
    print("No match")   # Readings differ significantly
