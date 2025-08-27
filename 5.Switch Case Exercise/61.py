'''input an alphabet and check whether it is vowel or consonant using switch case. '''

ch = input("Enter a character: ").strip()

match ch:
    case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | ' E'| 'I'| 'O' | 'U':
        print(str(ch)+" is a vowel.")
    case _:
        if ch.isalpha() and len(ch) == 1:
            print(str(ch)+" is a consonant.")
        else:
            print(str(ch)+" is not a alphabet.")