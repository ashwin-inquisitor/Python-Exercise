'''Input  two numbers from users and find the lcm using for loop.'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

max_num = max(num1, num2)

while(1):
    if max_num % num1 == 0 and max_num % num2 == 0:
        lcm = max_num
        break
    max_num += 1

print("The LCM of {} and {} is {}.".format(num1, num2, lcm))