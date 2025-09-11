'''Print inverted pyramid star pattern series using loop.'''

N = int(input("Enter number of rows for inverted pyramid: "))

for i in range(N, 0, -1):
    for j in range(N - i):
        print(" ", end=" ")

    for k in range(2 * i - 1):
        print("*", end=" ")
    print()