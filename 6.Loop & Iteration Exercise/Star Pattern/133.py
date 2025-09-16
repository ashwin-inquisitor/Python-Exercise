'''Print 8 star pattern series using loop.'''

size = int(input("Enter size: "))

for i in range(1, size * 2):
    for j in range(1, size + 1):
        if ((i == 1 and (j == 1 or j == size)) or (i == size and(j == 1 or j == size)) or (i == size * 2 - 1 and (j == 1 or j == size))):
            print(" ", end=" ")
        elif i == 1 or i == size or i == size * 2 - 1 or j == 1 or j == size:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()