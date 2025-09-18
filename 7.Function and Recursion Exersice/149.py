'''Find factorial of any number using recursion.'''

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

try:
    num = int(input("Enter number to find it's factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = fact(abs(num))
        print(f"Factorial of {num} is {result}.")

except ValueError:
    print("Invalid input! Please enter an integer.")