'''Write a program in python to convert decimal to binary number system.'''

decimal = int(input("Enter a decimal number: "))

if decimal == 0:
    print("Decimal equivalent is 0.")
else:
    binary = ''
    while decimal > 0:
        reminder = decimal % 2
        binary = str(reminder) + binary
        decimal = decimal // 2
    
    print("Decimal equivalent is ", binary)