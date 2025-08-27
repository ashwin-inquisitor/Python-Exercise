'''Input any number from user and print the reverse of the given number using loop.'''

num = int(input("Enter any number: "))
original = num
reverse = 0

while(original != 0):
    reverse = (reverse * 10) + (original % 10)
    original = original // 10

print("The revsere of {} is {}".format(num, reverse))