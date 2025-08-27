'''find all roots of a quadratic equation using if else.'''

import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2 * a)
    root2 = (-b - math.sqrt(D)) / (2 * a)
    print("Roots are real and distinct: ")
    print("Root 1 ="+str(root1))
    print("Root 2 ="+str(root2))
elif D == 0:
    root1 = root2 = -b / (2 * a)
    print("Root are real and equal: ")
    print("Root ="+str(root1))
else:
    real_part = -b /  (2 * a)
    imag_part = math.sqrt(-D) / (2 * a)
    print("Roots are complex and imaginary:")
    print("Root 1 = "+str(real_part)+" + "+str(imag_part)+" i.")
    print("Root 1 = "+str(real_part)+" - "+str(imag_part)+" i.")