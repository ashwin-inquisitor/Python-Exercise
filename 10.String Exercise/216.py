'''Remove all occurrences of a character from string.'''

str = input("Enter string: ")
char = input("Enter character to remove: ")

updated_str = str.replace(char, '')
print(f"Updated string: {updated_str}.")