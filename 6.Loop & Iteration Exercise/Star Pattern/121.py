'''Print hollor inverted mirrored right triangle star pattern using loop.'''

N = int(input("Enter number of rows for hollor inverted mirrored right triangle: "))

for i in range(N, 0, -1):
    for j in range(N - i):
        print(" ", end=" ")

    for k in range(1, i + 1):
        if k == 1 or k == i or i == N:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()