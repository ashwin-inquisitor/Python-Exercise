'''Remove last occurrence of a character from string.'''

str = input("Enter string: ")
char = input("Enter character to remove: ")

index = str.rfind(char)

if index != 1:
    updated_str = str[:index] + str[index+1:]
    print(f"Updated string: {updated_str}.")
else:
    print(f"Character '{char}' not found in string.")