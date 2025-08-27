'''Input a number and calculate the factorial using for loop.'''

num = int(input("Enter any number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i
print("Factorial {} of is {}.".format(num, fact))