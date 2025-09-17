'''Find prime numbers between two interval using function.'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_upto(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

try:
    upper_limit = int(input("Enter upper limit to find prime: "))
    prime_numbers = find_prime_upto(upper_limit)

    print(f"Prime numbers upto {upper_limit}:")
    print(prime_numbers)

except ValueError:
    print("Invalid input! Please enter a interge.")