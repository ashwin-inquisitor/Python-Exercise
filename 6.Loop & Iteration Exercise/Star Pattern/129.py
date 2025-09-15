'''Print Hollow diamond star pattern series using loop.'''

N = int(input("Enter number of rows for hollow diamond star:  "))

for i in range(N, 0, -1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2 * (N - i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(1, N + 1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2 * (N - i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()