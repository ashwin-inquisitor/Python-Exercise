'''Generate nth Fibonacci term using recursion.'''
def fib(n):
    if n <= 0:
        return "Invalid input! Number must be positive."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


try:
    num = int(input("Enter position of the fibonacci term: "))
    result = fib(num)
    print(f"{num}th fibonacci term is: {result}.")

except ValueError:
    print("Invalid input! Please enter an integer: ")