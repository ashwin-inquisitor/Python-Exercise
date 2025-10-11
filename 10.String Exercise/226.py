'''Remove last occurrence of a word in given string.'''

str = input("Enter string: ")
word = input("Enter word to remove: ")

index = str.rfind(word)

if index != -1:
    updated_str = str[:index] + str[index + len(word):]
    print(f"Updated string: {updated_str.strip()}")
else:
    print(f"Word '{word}' not found in string.")