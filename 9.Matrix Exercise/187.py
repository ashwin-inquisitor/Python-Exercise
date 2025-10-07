'''Find sum of upper triangular matrix.'''

n = int(input("Enter size of square matrix n * n: "))

print("Enter matrix elements row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(n)]

upper_sum = 0
for i in range(n):
    for j in range(i, n):
        upper_sum += matrix[i][j]

print(f"Sum of upper triangular matrix is {upper_sum}.")