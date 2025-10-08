'''Compare two strings.'''

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1.lower() == str2.lower():
    print("Two strings are equal (case-insensetive).")
else:
    print("Two strings are not equal.")