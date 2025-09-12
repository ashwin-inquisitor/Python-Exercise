'''Print half diamond star pattern series using loop.'''

N = int(input("Enter the number of rows for half diamond star: "))

for i in range(1, N + 1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(N - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()