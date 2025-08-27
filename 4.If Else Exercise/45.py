'''to check whether an alphabet is vowel or consonant using if else.'''

letter = input("Enter any charcter : ")

if len(letter) == 1 and letter.isalpha():
    if letter.lower() in ['a', 'e','i', 'o', 'u']:
        print("letter is vowel.")
    else:
        print("letter is consonant.") 