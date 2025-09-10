'''Print mirrored right triangle star pattern series using loop.'''

N = int(input("Enter number of rows for mirroed right triangle: "))

for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end=" ")

    for k in range(i):
        print("*", end=" ")
    print()