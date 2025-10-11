'''Find first occurrence of a word in a given string.'''

str = input("Enter string: ")
word = input("Enter word to find: ")

index = str.find(word)

if index != -1:
    print(f"First occurrence of '{word}' is at index {index}.")
else:
    print(f"Word '{word}' not found in string.")