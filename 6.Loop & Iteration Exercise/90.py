'''Input a number and check whether the number is prime or not using for loop.'''

num = int(input("Enter any number: "))

if num < 2:
    print("{} is not prime.".format(num))
else:
    isprime = 1
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            isprime = False
            break

if isprime:
    print("{} is prime.". format(num))
else:
    print("{} is not prime.".format(num))