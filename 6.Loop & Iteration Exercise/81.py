'''Input number from user and check number is pailndrome or not using loop. '''

num = int(input("Enter any number: "))
original = num
reverse = 0

while (original!=0):
    reverse = (reverse * 10) + (original % 10)
    original = original // 10

if reverse == num:
    print("{} is palnidrome of {}.".format(reverse, num))
else:
    print("{} is not palnidrome of {}.".format(reverse, num))