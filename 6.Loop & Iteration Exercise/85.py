'''Find  power of a number using for loop.'''

base = int(input("Enter the base number:"))
exponent = int(input("Enter the exponent: "))

result = 1

for _ in range(exponent):
    result *= base

print("{} raised to power {} is {}".format(base, exponent, result))