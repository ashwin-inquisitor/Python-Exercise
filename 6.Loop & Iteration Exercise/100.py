'''Write a program in python to convert Binary to Hexadecimal number system.'''

binary = input("Enter a binary number: ")

if not all(bit in '01' for bit in binary):
    print("Invalid binary number! Enter number in 0s and 1s format.")
else:
    while len(binary) % 4 != 0:
        binary = '0' + binary
    
    hexadecimal = ''
    i = 0

    while i < len(binary):
        four_bits = binary[i:i+4]
        decimal = 0
        power = 3

        for bit in four_bits:
            decimal += int(bit) * (2 ** power)
            power -= 1

        if decimal < 10:
            hex_digit = str(decimal)
        else:
            hex_digit = chr(ord('A') + decimal - 10)

        hexadecimal += hex_digit
        i += 4

print("Hexadecimal equivalent : ", hexadecimal)