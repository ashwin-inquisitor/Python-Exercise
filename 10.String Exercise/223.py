'''Search all occurrences of a word in given string.'''

str = input("Enter string: ")
word = input("Enter word to search: ")

position = []
start = 0

while True:
    index = str.find(word, start)
    if index == -1:
        break
    position.append(index)
    start = index +  len(word)

if position:
    print(f"'{word}' at positions: {position}")
else:
    print(f"'{word}' not found in string.")