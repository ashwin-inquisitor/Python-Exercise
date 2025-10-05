'''Add two matrices.'''
rows = int(input("Rows: "))
cols = int(input("columns: "))

print("Enter matrix A: ")
A = [[int(x) for x in input().split()] for _ in range(rows)]

print("Enter matrix B: ")
B = [[int(x) for x in input().split()] for _ in range(rows)]

C = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

print("Result:")
for row in C:
    print(*row)