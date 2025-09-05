'''Write a program in python to convert decimal to hexadecimal number system.'''

decimal = int(input("Enter a decimal number: "))

if decimal == 0:
    print("Hexadecimal equivalent is 0.")
else:
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexa_digit = str(remainder)
        else:
            hexa_digit = chr(ord('A') + remainder - 10)
        hexadecimal = hexa_digit + hexadecimal
        decimal = decimal // 16

    print("Hexadecimal equivalent is {}.".format(hexadecimal))