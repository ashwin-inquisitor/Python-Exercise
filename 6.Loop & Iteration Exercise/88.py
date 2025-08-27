'''Input two number from user and find the HCF using for loop.'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
hcf = 1

min_num = min(num1, num2)

for i in range(1, min_num + 1):
    if num1 % i == 0 and num2 % i ==0:
        hcf = i

print("The HCF of {} and {} is {}.".format(num1, num2, hcf))