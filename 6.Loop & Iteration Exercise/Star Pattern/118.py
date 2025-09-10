'''Print inverted right triangle star pattern using loop.'''

N = int(input("Enter number of rowsnn for inverted right triangle: "))

for i in range(N, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()