'''Print hollow right triangle star pattern series using loop.'''

N = int(input("Enter number of rows for hollow right triangle: "))

for i in range(1, N + 1):
    for j in range(1, i + 1):
        if i == 0 or j == 1 or j == i or i == N :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()