'''Find lowest frequency character in a string.'''

str =  input("Enter string: ")

frequency = {}

for char in str:
    if char != ' ':
        frequency[char] = frequency.get(char, 0)+ 1

min_count = min(frequency.values())
min_char = [char for char, count in frequency.items() if count == min_count]

print(f"Lowest frequency character: '{min_char}' occurs {min_count} time(s). ")