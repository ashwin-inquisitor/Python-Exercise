'''Count total number of vowels and consonants in a string.'''

str = input("Enter string: ").lower()

vowel = consonant = 0

for char in str:
    if char.isalpha():
        if char in 'aeiou':
            vowel += 1
        else:
            consonant += 1

print(f"Vowels: {vowel}")
print(f"Consonants: {consonant}")