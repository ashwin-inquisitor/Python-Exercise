'''Count occurrences of a word in a given string.'''

str = input("Enter string: ")
word = input("Enter word to count: ")

count = str.count(word)

print(f"The word '{word}' occurs {count} time(s).")