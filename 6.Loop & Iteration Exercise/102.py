'''Write a program in python to convert decimal to octal number system.'''

decimal = int(input("Enter a decimal number:"))

if decimal == 0:
    print("Decimal equivalent is 0.")
else:
    octal = ''
    while decimal > 0:
        reminder = decimal % 8
        octal = str(reminder) + octal
        decimal = decimal // 8

    print("Decimal equivalent is {}.".format(octal))
