'''Enter a side of a equilateral triangle and find it's area.'''

import math

s = int(input("Enter the side of a triangle: "))

area = (math.sqrt(3) / 4) * s ** 2

print("Area of an equilateral triangle is {:.2f}".format(area))