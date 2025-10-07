'''Check Sparse matrix.'''

rows = int(input("Rows: "))
cols = int(input("Columns: "))
print("Enter matrix elements row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

zero_count = sum(1 for i in range(rows) for j in range(cols) if matrix[i][j] == 0)
total_elements = rows * cols

if zero_count > total_elements / 2:
    print("Matrix is sparse matrix.")
else:
    print("Mateix is Not sparse matrix.")
    