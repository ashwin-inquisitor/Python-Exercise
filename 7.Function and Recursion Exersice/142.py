'''Print all natural numbers between 1 to n using recursion.'''
def print_natural_numbers (n , current = 1):
    if current > n:
        return
    print(current)
    print_natural_numbers(n, current + 1)


try:
    n = int(input("Enter upper limit: "))
    if n < 1:
        print("Please enter number greater than or equal to 1.")
    else:
        print(f"Natural number from 1 to {n}:")
        print_natural_numbers(n)
except ValueError:
    print("Invalid input! Please enter valid integer.")