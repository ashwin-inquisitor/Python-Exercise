'''Remove first occurrence of a character from string.'''

str = input("Enter string: ")
char = input("Enter character to remove: ")

if char in str:
    updated_str = str.replace(char, '', 1)
    print(f"Updated string: {updated_str}.")
else:
    print(f"Character '{char}' not found in string.")