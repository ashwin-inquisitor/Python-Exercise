'''print hollow rhombus star pattern of N rows using for loop'''

N = int(input("Enter number of rows for hollow star pattern: "))

for i in range(N):
    for j in range(N - i - 1):
        print(" ", end=" ")
    for k in range(N):
        if i == 0 or i == N - 1 or k == 0 or k == N - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()