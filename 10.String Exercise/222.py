'''Find last occurrence of a word in a given string.'''

str = input("Enter string: ")
word = input("Enter word to find: ")

index = str.rfind(word)

if index != -1:
    print(f"Last occurrence of '{word}' is at index {index}.")
else:
    print(f"Word '{word}' not found in index.")