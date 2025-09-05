'''Write a program in python to convert binary to decimal number system.'''

binary = input("Enter a binary number: ")

if not all(bit in '01' for bit in binary):
    print("Invalid binary number! Enter number in 0s and 1s format.")
else:
    decimal = 0
    power = len(binary) - 1

    for bit in binary:
        decimal += int(bit) * (2 ** power)
        power -= 1
    
    print("Decimal equivalent: ", decimal)