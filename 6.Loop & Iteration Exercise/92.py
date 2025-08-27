'''Input a number from a user and find all the prime factor of the given number using loop.'''

num = int(input("Enter any number: "))

for i in range(2, num+1/2):
    if num % i == 0:
        isprime = 1
        for n in range(2, int(num**0.5)+1):
            if i % n == 0:
                isprime = False
                break
if isprime:
    print(i)
