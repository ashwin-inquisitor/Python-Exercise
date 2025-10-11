'''Replace last occurrence of a character with another in a string.'''

str = input("Enter string: ")
old_char = input("Enter character to replace: ")
new_char = input("Enter new character: ")

index = str.rfind(old_char)

if index != -1:
    updated_str = str[:index]+ new_char + str[index+1:]
    print(f"Updated string: {updated_str}")
else:
    print(f"Character {old_char} not found in string.")