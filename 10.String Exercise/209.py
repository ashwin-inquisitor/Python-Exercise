'''Search all occurrences of a character in given string.'''

str = input("Enter string: ")
char = input("Enter character to search: ")

position = []

for index, c in enumerate(str):
    if c == char:
        position.append(index)
if position:
    print(f"Character '{char}'  found at positions: {position}.")
else:
    print(f"Character '{char}' not found in string.")