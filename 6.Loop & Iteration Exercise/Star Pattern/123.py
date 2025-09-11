'''Print hollow pyramid star pattern series using loop.'''

N = int(input("Enter number of rows for hollow pyramid: "))

for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end=" ")

    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == N:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()