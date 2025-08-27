'''print natural number in reverse in given range'''

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

i = start

while i >= end:
    print(i)
    i -= 1