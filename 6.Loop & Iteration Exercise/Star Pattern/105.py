'''print square star(*) pattern series of N rows.'''

N = int(input("Enter the number of rows: "))

for i in range(N):
    for j in range(N):
        print("*" , end=" ")
    print()