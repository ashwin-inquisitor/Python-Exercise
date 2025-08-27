'''input sides of a triangle and check 
whether a triangle is equilateral, scalene 
or isosceles triangle using if else.'''

A = int(input("Enter the side of triangle : "))
B = int(input("Enter the side of triangle : "))
C = int(input("Enter the side of triangle : "))

if A == B & B == C:
    print("Triangle is equilateral.")
elif A == B or B == C or A == C:
    print("Triangle is isosceles.")
else:
    print("Triangle is scalene.")