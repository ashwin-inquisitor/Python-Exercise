'''Find upper triangular matrix.'''

n = int(input("Enter size of squuare matrix n * n: "))

print("Enter matrix elements row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(i):
        matrix[i][j] = 0

print("upper triangular matrix: ")
for row in matrix:
    print(*row)