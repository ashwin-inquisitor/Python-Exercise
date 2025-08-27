'''Input a number from user and calculate the product of its digits using loop.'''

num = int(input("Enter any number: "))
product = 1

while (num != 0):
    product *= num % 10
    num = num // 10

print("Product of digits is ", product)