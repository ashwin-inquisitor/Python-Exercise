'''Program to find two's complement of a binary number.'''

binary = input("Enter binary number: ")

ones_complement = ""
valid = True

for bit in binary:
    if bit == '0':
        ones_complement += '1'
    elif bit == '1':
        ones_complement += '0'
    else:
        print("Invaild binary digit detected!")
        valid = False
        break

if valid:
    twos_complement = list(ones_complement)
    carry = 1

    for i in range(len(ones_complement)-1,-1,-1):
        if twos_complement[i] == '1' and carry == 1:
            twos_complement[i] = '0'
        elif twos_complement[i] == '0' and carry == 1:
            twos_complement[i] = '1'
            carry =0
        
    if carry == 1:
        twos_complement.insert(0, '1')

    result = ''.join(twos_complement)
    print("Two's complement of {} is {}.".format(binary,result))