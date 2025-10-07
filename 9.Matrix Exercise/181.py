'''Find sum of main diagonal elements of a matrix.'''

n = int(input("Enter size of square matrix n * n : "))

print("Matrix elements row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(n)]

diagonal_sum = sum(matrix[i][i] for i in range(n))

print(f"sum of main diagonal elements is {diagonal_sum}.")