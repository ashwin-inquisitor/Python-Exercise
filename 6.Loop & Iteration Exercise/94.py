'''Print armstrong number between 1 to n.'''

num = int(input("Enter any number: "))

for i in range(1, num + 1):
    original = num
    count = 0
    sum = 0

    while original > 0:
        count += 1
        original //= 10
        

    original = num

    while original > 0:
        digit = original % 10
        sum += original ** count
        original //= 10

if sum == num:
    print(num, end=' ')
