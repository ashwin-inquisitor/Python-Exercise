'''Find lower triangular matrix.'''
n = int(input("Enter size of square matrix n * n: "))

print("Enter matrix elements row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j] = 0

print("Lower triangular matrix: ")
for row in matrix:
    print(*row)