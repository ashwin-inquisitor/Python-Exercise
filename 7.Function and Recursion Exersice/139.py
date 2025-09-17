'''Check whether a number is prime, armstrong, perfect number or not using functions. '''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
         return False
    return True

def is_armstrong(n):
   digits = [int(d) for d in str(n)]
   power = len(digits)
   return sum(d ** power for d in digits) == n

def is_perfect(n):
   if n < 2:
      return False
   return sum(i for i in range(1, n) if n % 1 == 0) == n

try:
   number = int(input("Enter number: "))

   print(f"Prime number: {'Yes' if is_prime(number) else 'No'}.")
   print(f"Armstrong number: {'Yes' if is_armstrong(number) else 'No'}.")
   print(f"Prefect number: {'Yes' if is_perfect(number) else 'No'}.")

except ValueError:
   print("Invalid input! Please enter valid integer.")