'''input side of a triangle and check whether triangle is valid or not using if else.'''

A = int(input("Enter the side of triangle : "))
B = int(input("Enter the side of triangle : "))
C = int(input("Enter the side of triangle : "))

if A + B > C and A + C > B and B + C > A:
    print("Triangle is valid.")
else:
    print("Invalid triangle.")