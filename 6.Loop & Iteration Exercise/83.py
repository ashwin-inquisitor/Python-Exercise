'''Input a number from user and print it in words using for loop.'''

num = input("Enter any number: ")
digit_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

print("Number in words")
for digit in num:
    if digit.isdigit():
        print(digit_words[int(digit)], end=' ')
    else:
        print("Invalid input!")