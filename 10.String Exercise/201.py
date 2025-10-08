'''Find total number of alphabets, digits or special character in a string.'''

str = input("Enter string:")

alphabets = digits = special = 0

for char in str:
    if char.isalpha():
        alphabets  += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1

print(f"Alphabets: {alphabets}")
print(f"Digits: {digits}")
print(f"Special character: {special}")