'''Count occurrences of a character in given string.'''

str = input("Enter string: ")
char = input("Enter character to count:  ")

count = str.count(char)

print(f"Charater '{char}' occurs {count} time(s) in string.")