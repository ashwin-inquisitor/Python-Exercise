'''Write a program in python to convert octal to binary number system.'''

octal = input("Enter a octal number: ")

if not all(digit in '01234567' for digit in octal):
    print("Invalid octal number! Enter number between 0 to 7.")
else:
    binary = ''
    for digit in octal:
        decimal_value = int(digit)
        binary_chunk = ''
        power = 2
        while power >= 0:
            bit = decimal_value // (2 ** power)
            binary_chunk += str(bit)
            decimal_value = decimal_value % (2 ** power)
            power -= 1
        binary += binary_chunk
    print("Binary equivalent is {}.".format(binary))