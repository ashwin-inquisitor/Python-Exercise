'''Find sum of each row and column of a matrix.'''

rows = int(input("Rows: "))
cols = int(input("Columns: "))

print("Enter matrix elements row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

print("Sum of each row: ")
for i in range(rows):
    print(f"Row {i + 1}: {sum(matrix[i])}.")

print("\nSum of each columns: ")
for j in range(cols):
    cols_sum = sum(matrix[i][j] for i in range(rows))
    print(f"Columns {j + 1}: {cols_sum}.")