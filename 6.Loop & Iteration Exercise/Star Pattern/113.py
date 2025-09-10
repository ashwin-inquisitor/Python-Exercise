'''print hollow mirrored rhombus star pattern series of N rows using for loop.'''

N = int(input("Enter the number of rows: "))

for i in range(N):
    for j in range(i):
        print(" ", end=" ")
    for k in range(N):
        if i == 0 or i == N - 1 or k == 0 or k == N - 1:
                print("*", end=" ")
        else:
             print(" ", end=" ")
    print()