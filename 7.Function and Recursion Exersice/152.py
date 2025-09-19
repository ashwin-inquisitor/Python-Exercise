'''Find LCM of two numbers using recursion.'''
def lcm(a, b, multiple = None):
    if multiple is None:
        multiple = max(a, b)
    if multiple % a == 0 and multiple % b == 0:
        return multiple
    return lcm(a, b, multiple + 1)

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 == 0 and num2 == 0:
        print("Lcm undefined when either number is zero.")
    else:
        result = lcm(num1, num2)
        print(f"LCM of {num1} and {num2} is {result}.")

except ValueError:
    print("Invalid input! Please enter an integer.")