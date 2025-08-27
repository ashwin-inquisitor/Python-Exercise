'''input a character and check whether the character is 
alphabet or not using Conditional/Ternary operator '''

char = input("Enter a character : ")

result = "Invalid input! Please enter only one character." if len(char) !=1 else ("Alphabet" if char.isalpha() else "Not an alphabet")

print(result)