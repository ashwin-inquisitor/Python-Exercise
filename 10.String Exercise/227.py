'''Remove all occurrence of a word in given string.'''

str = input("Enter string: ")
word = input("Enter word to remove: ")

updated_str = str.replace(word, '')
print(f"Updated string: {updated_str.strip()}")