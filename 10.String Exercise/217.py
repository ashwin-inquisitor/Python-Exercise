'''Remove all repeated characters from a given string.'''

str = input("Enter string: ")

frequency = {}
for char in str:
    frequency[char] = frequency.get(char, 0)+ 1

result = ''.join([char for char in str if frequency[char] == 1])

print(f"String after removing repeated characters: {result}")