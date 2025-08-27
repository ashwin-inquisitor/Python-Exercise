'''input a character from user and 
check whether given character is alphabet, 
digit or special character using if else.'''

char = input("Enter a charcter : ")
if len(char) !=1:
    print("Please enter only one charcter.")
else:
    if char.isalpha():
        print("Char is alphabet.")
    elif char.isdigit():
        print("Char is digit.")
    else:
        print("Char is special charcter.")