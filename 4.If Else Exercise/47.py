'''input character from user and check whether 
character is uppercase or lowercase alphabet using if else. '''

char = input("Enter a charcter : ")

if len(char) !=1 or not char.isalpha():
    print("Invalid input! Please enter a single charcter.")
else:
    if char.isupper():
        print(str(char)+" is a uppercase alphabet.")
    else:
        print(str(char)+" is a lowercase alphabet.")