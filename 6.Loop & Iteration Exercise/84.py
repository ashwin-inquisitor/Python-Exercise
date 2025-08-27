'''Print ASCII values of all the charcters using for loops.'''

print("ASCII values of all character from 0 to 255:\n")

for i in range(255):
    ascii_char = chr(i)
    print(str(i).rjust(3), ":", repr(ascii_char))