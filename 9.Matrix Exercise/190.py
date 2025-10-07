'''Find determinant of a matrix.'''

n = int(input("Enter size of square matrix (2 or 3): "))
print("Enter matrix elements row-wise: ")
matrix = [[int(x) for x in input().split()] for _ in range(n)]

if n==2:
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
elif n == 3:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    det = a*(e*i - f*h) - b*(d*i - g*f) + c*(d*h - e*g)

else:
    print("Only 2x2 or 3x3 matrices supported in this version.")
    det = None

if det is not None:
    print("Determinant:", det)