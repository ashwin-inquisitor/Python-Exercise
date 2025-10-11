'''Remove all extra blank spaces from given string.'''

str = input("Enter string: ")

clean_str = ' '.join(str.split())
print(f"String after removing extra spaces: {clean_str}")