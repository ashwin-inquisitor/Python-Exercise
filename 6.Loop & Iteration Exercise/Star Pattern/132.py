'''Print plus star pattern series using loop.'''

N = int(input("Enter odd number for size: "))

if N % 2 == 0:
    print("Please! Enter odd number.")
else:
    mid = N // 2
    for i in range(N):
        for j in range(N):
            if i == mid or j == mid:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()