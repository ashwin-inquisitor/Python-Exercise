'''Check whether two matrices are equal or not.'''

rows = int(input("Rows: "))
cols = int(input("Columns: "))

print("Enter Matrix A:")
A = [[int(x) for x in input().split()] for _ in range(rows)]
print("Enter Matrix B:")
B = [[int(x) for x in input().split()] for _ in range(rows)]

equal = True
for i in range(rows):
    for j in range(cols):
        if A[i][j] != B[i][j]:
            equal = False
            break

print("Matrices are equal" if equal else "Matrices are not  equal.")
