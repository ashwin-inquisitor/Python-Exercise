'''Print a diamond star pattern series using loop.'''

N = int(input("Enter number of rows for diamond star: "))

for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end=" ")
    for k in range(2 * i -1):
        print("*", end=" ")
    print()

for i in range(N - 1, 0, -1):
    for j in range(N - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()