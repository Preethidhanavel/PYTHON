'''Task: Write a Python program to create a 3x3 matrix using nested list comprehensions.
Sample input: Rows: 3, Columns: 3
Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]'''
rows = int(input("rows: "))
col = int(input("columns: "))

matrix = [] 
print("entries row-wise:")

for i in range(rows):   
    row = []
    for j in range(col):
        row.append(int(input("Enter element")))    
    matrix.append(row) 

print("\n2D matrix is:")

for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()