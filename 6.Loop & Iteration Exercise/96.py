'''Program to find one's complement of a binary number.'''

n = input("Enter number: ")

ones_complement = ""
valid = True

for bit in n:
    if bit == '0':
        ones_complement += '1'
    elif bit == '1':
        ones_complement += '0'
    else:
        print("Invalid binary digit detected!")
        valid = False
        break

if valid:
    print("One's complement of {} is {}".format(n,ones_complement))