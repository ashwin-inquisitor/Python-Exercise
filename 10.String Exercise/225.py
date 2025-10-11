'''Remove first occurrence of a word from string.'''

str = input("Enter string: ")
word = input("Enter word to remove: ")

index = str.find(word)

if index != -1:
    updated_str = str[:index] + str[index + len(word):]
    print(f"Updated string: {updated_str.strip()}")
else:
    print(f"Word '{word}' not found in string.")