'''Find sum of all prime numbers between 1 to n using for loop.'''

num = int(input("Find the sum of all prime numbers between 1 to: "))
sum = 0

for i in range(2, num + 1):
    isprime = True
    for n in range(2, int(num**0.5)+1):
        if i % n == 0:
            isprime = False
            break
    if isprime:
        sum += num

print(sum)
