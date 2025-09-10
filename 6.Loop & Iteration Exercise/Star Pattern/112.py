'''print inverted/mirrored rhombus star pattern series using for loop.'''

N = int(input("Enter number of rows for hollow star: "))

for i in range(N):
    for j in range(i):
        print(" ", end=" ")
    for k in range(N):
        print("*", end=" ")
    print()