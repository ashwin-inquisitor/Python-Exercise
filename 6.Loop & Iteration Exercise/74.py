'''input a number from user and count number of digits in the given integer using loop.'''

num = int(input("Enter a number: "))
count = 0

if num == 0:
    count = 1
else:
    num = abs(num)

    while num > 0:
        num //=10
        count += 1
        
print("Number of digits:", count)