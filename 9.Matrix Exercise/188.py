'''Find sum of lower triangular matrix.'''

n = int(input("Enter size of square matrix n * n: "))

print("Enter matrix elements row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(n)]

lower_sum = 0
for i in range(n):
    for j in range(i + 1):
        lower_sum += matrix[i][j]

print(f"Sum of lower triangluar matrix: {lower_sum}.")