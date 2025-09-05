'''Write a program in python to convert binary to octal number system.'''

binary = input("Enter a binary number: ")

if not all(bit in '01' for bit in binary):
    print("Invalid binary number! Enter number in 0 and 1 format.")
else:
    while len(binary) % 3 !=0:
        binary = '0' + binary

    octal = ''
    i = 0
    while i < len(binary):
        three_bits = binary[i:i+3]
        decimal = 0
        power = 2
        for bit in three_bits:
            decimal += int(bit) * (2 ** power)
            power -= 1
        octal += str(decimal)
        i += 3
        
    print("Octal equivalent: ", octal)