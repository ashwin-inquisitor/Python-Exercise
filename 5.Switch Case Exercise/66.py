'''create menu driven calculator that performs basic arithmetic operations 
(add, subtract, multiply and divide) using switch case and functions. '''

import math

num2 = float(input("Enter a first number: "))
num1 = float(input("Enter a second number: "))
op = input("Enter operation to perform from [+ - * /]: ")

match op:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        result = num1 / num2
    case _:
        print("Invalid input!")

print("result:",result)