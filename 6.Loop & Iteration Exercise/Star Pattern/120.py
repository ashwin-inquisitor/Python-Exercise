'''Print inverted mirrored right triangle star pattern using loop.'''

N = int(input("Enter the number of rows for inverted mirrored right triangle: "))

for i in range(N, 0, -1):
    for j in range(N - i):
        print(" ", end=" ")

    for k in range(i):
        print("*", end=" ")
    print()