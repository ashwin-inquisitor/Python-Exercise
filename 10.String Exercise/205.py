'''Check whether a string is palindrome or not.'''

str = input("Enter string: ")
reversed_str = str[::-1]

if str == reversed_str:
    print("String is palindrome.")
else:
    print("String is not palindrome.")