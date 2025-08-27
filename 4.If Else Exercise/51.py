'''check whether a triangle is valid or not if angles are given using if else.'''

A = int(input("Enter the angle of triangle : "))
B = int(input("Enter the angle of triangle : "))
C = int(input("Enter the angle of triangle : "))

sum_of_angles = A + B + C

if sum_of_angles == 180 and A > 0 and B > 0 and C > 0:
    print("Triangle is valid.")
else:
    print("Invalid triangle.")