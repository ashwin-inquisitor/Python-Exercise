'''Write a program in python to convert decimal to octal number system.'''

decimal = int(input("Enter a decimal number:"))

if decimal == 0:
    print("Octal equivalent is 0.")
else:
    octal = ''
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal = decimal // 8

    print("Octal equivalent is {}.".format(octal))
