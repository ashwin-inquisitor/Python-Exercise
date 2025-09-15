'''Print right arrow star pattern series using loop.'''

N = int(input("Enter number of row: "))

for i in range(1, N + 1):
    for j in range(2 * (i - 1)):
        print(" ", end=" ")
    for k in range(N - i + 1):
        print("*", end=" ")
    print()

for i in range(N - 1, 0, -1):
    for j in range(2 * (i - 1)):
        print(" ", end=" ")
    for k in range(N - i + 1):
        print("*", end=" ")
    print()