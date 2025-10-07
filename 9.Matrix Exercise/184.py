'''Interchange diagonals of a matrix.'''

n = int(input("Enter size of square matrix n * n: "))

print("Enter elements of matrix row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[i][n - i - 1] =  matrix[i][n - i - 1], matrix[i][i]

print("Matrix after interchanging diagonals: ")
for row in matrix:
    print(*row)