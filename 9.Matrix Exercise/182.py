'''Find sum of minor diagonal elements of a matrix.'''

n = int(input("Enter size of square matrix n * n: "))

print("Enter matrix elements row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(n)]

minor_diagonal_sum = sum(matrix[i][n - 1 - i] for i in range(n))

print(f"Sum of minor diagonal is {minor_diagonal_sum}.")