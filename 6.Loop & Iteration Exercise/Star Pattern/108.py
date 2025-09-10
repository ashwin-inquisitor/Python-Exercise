'''print hollow rectangle star(*) pattern series using for loop.'''

N = int(input("Enter the number of rows for hollow rectangle: "))
M = int(input("Enter the number of columns for hollow rectangle: "))

for i in range(N):
    for j in range(M):
        if i == 0 or i == N - 1 or j == 0 or j == M - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()