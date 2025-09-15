'''Print left arrow star pattern using loop.'''

N = int(input("Enter number of rows: "))

for i in range(N, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(2, N + 1):
    for j in range(i):
        print("*", end=" ")
    print()