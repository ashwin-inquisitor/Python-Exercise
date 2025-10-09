'''Find highest frequency character in a string.'''

str = input("Enter string: ")

frequency = {}

for char in str:
    if char != ' ':
        frequency[char] = frequency.get(char, 0)+ 1

max_count = max(frequency.values())
max_char = [char for char, count in frequency.items() if count == max_count]

print(f"Highest frequncy charater: '{max_char}' occurs {max_count} time(s).")