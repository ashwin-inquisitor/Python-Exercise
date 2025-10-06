'''Multiply two matrices.'''
rows1 = int(input("Rows: "))
cols1 = int(input("columns: "))
rows2 = int(input("Rows: "))
cols2 = int(input("columns: "))

if cols2 != rows1:
    print("Martix multiplician not possible. columns of A must equal rows of B.")
else:
    print("Enter Martrix A: ")
    A = [[int(x) for x in input().split()] for _ in range(rows1)]

    print("Enter Martrix B: ")
    B = [[int(x) for x in input().split()] for _ in range(rows2)]

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += A[i][k] * B[k][j]

    print("Result: ")
    for row in result:
        print(*row)