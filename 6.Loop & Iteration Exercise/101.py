'''Write a program in python to convert decimal to binary number system.'''

decimal = int(input("Enter a decimal number: "))

if decimal == 0:
    print("Binary equivalent is 0.")
else:
    binary = ''
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    
    print("Binary equivalent is ", binary)