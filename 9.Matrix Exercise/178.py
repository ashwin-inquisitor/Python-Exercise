'''Perform Scalar matrix multiplication.'''
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

print("Matcix: ")
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

scalar = int(input("Enter scalar value: "))

result = [[scalar * matrix[i][j] for j in range(rows)] for i in range(rows)]

print("Result: ")
for row in result:
    print(*row)