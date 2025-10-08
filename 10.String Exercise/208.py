'''Find last occurrence of a character in a given string.'''

str = input("Enter string: ")
char = input("Enter character to find: ")

index = str.rfind(char)

if index != -1:
    print(f"Last occurrence of character '{char}' is at index {index}.")
else:
    print(f"Character {char} not found in the string.")