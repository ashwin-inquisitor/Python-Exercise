'''Find GCD (HCF) of two numbers using recursion.'''
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b,  a % b)

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if(num1 == 0 and num2 == 0):
        print("GCD is undefined for both number being zero.")
    else:
        result = gcd(abs(num1), abs(num2))
        print(f"GCD of {num1} and {num2} is {result}.")
except ValueError:
    print("Invalid input! Please enter an integer.")