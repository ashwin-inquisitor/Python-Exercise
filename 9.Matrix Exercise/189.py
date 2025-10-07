''' Find transpose of a matrix.'''

rows = int(input("Rows: "))
cols = int(input("Columns: "))

print("Enter matrix elements row-wise: ")
matrix =  [[int(x) for x in input().split()] for _ in range(rows)]

transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

print("Transpose of the matrix: ")
for row in transpose:
    print(*row)