'''Check Symmetric matrix.'''

n = int(input("Enter size of square matrix (nxn): "))
print("Enter matrix elements row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(n)]

is_symmeyric = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_symmeyric = False
            break

print("Matrix is symmetric matrix." if is_symmeyric else "Matrix is Not symmetric matrix.")