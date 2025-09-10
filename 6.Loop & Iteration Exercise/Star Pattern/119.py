'''Print hollow inverted right triangle star pattern using loop.'''

N = int(input("Enter number of rows for hollow inverted right triangle: "))

for i in range(N, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == N:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()