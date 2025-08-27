'''input two numbers from user and find maximum between two numbers using switch case. '''

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

match(a > b, a < b):
    case (True,False):
        print("Maximum is ",a )
    case (False, True):
        print("Maximum is ",b)
    case _:
        print("Both are equal.")