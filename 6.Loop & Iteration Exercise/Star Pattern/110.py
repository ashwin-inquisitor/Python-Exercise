'''print rhombus star pattern of N rows using for loop.'''

N = int(input("Enter number of rows for rhombus pattern: "))

for i in range(N):
    for j in range(N - i - 1):
        print(" ", end=" ")
    for k in range(N):
        print("*", end=" ")
    print()