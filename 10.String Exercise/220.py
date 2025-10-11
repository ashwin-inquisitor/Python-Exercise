'''Replace all occurrences of a character with another in a string.'''

str = input("Enter string: ")
old_char = input("Enter character to replace: ")
new_char = input("Enter new character: ")

updated_str = str.replace(old_char, new_char)
print(f"Updated string: {updated_str}")