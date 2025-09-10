'''print rectangle star(*) pattern in C of N rows and M columns.'''

N = int(input("Enter the number of rows: "))
M = int(input("Enter the number of columns: "))

for i in range(N):
    for i in range(M):
        print("*", end=" ")
    print()