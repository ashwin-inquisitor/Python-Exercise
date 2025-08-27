'''Input a number from user and print multiplication table of the given number using for loop.'''

num = int(input("Enter a number: "))

print("Multiplication table of {num}")
for i in range(1, 11):
    print("{} x {} = {}".format(num, i, num*i))