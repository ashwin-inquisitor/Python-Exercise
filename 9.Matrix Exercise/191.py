'''Check Identity matrix.'''

n = int(input("Enter size of square matrix (nxn): "))
print("Enter matrix elements row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(n)]

is_identity = True
for i in range(n):
    for j in range(n):
        if(i == j and matrix[i][j] != 1) or(i != j and matrix[i][j] != 0):
            is_identity = False
            break
        
print("Matrix is an identity matrix" if is_identity else "Matrix is Not an identity.")