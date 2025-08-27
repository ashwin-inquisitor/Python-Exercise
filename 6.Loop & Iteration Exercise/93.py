'''Input a number from a user and check whether the given number is armstrong or not.'''

num = int(input("Enter any number: "))
original = num
count = 0
sum = 0

while original > 0:
    original //= 10
    count += 1

original = num
while original > 0:
    digit = original % 10
    sum += digit ** count
    original //= 10

if sum == num:
    print("{} is armstrong.".format(num))
else:
    print("{} is not armstrong.".format(num))