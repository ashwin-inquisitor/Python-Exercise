'''print hollow square star pattern with diagonal using loops.'''

N = int(input("Enter size of the square: "))

for i in range(N):
    for j in range(N):
        if i == 0 or i == N - 1 or j == 0 or j == N - 1 or i == j or i + j == N - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()