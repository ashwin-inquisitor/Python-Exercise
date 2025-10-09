'''Count frequency of each character in a string.'''

str = input("Enter string: ")

frequency = {}

for char in str:
    if char != ' ':
        frequency[char] = frequency.get(char, 0)+ 1

print("Character frequencies: ")
for char, count in frequency.items():
    print(f"'{char}': {count}.")