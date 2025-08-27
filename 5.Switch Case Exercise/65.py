'''find all roots of a Quadratic equation using switch case.'''

import math

a = int(input("Enter the coffeicient a: "))
b = int(input("Enter the coffeicient b: "))
c = int(input("Enter the coffeicient c: "))

D = b ** 2 - 4 * a * c

match(D > 0, D == 0, D < 0):
    case (True, False, False):
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        print("Roots are real and distinct: ")
        print("Root 1 is {:.2f}".format(root1))
        print("Root 2 is {:.2f}".format(root2))
    case (False, True, False):
        root1 = root2 = -b / (2 * a)
        print("Root are real and equal: ")
        print("Root is {:.2f}".format(root1))
    case (False, False, True):
        real_part = -b /  (2 * a)
        imag_part = math.sqrt(-D) / (2 * a)
        print("Roots are complex and imaginary:")
        print("Root 1 = "+str(real_part)+" + "+str(imag_part)+" i.")
        print("Root 1 = "+str(real_part)+" - "+str(imag_part)+" i.")
