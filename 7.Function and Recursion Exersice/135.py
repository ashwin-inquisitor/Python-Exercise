'''find diameter, circumference snd area of circle using functon.'''

import math

def get_diameter(radius):
  return 2 * radius

def get_circumference(radius):
  return 2 * math.pi * radius

def get_area(radius):
  return math.pi * radius ** 2

radius = float(input("Enter raduis of the circle: "))

diameter = get_diameter(radius)
circumference = get_circumference(radius)
area = get_area(radius)

print(f"Daimeter of circle: {diameter}")
print(f"Circumference of circle: {circumference:.2f}")
print(f"Area of circle: {area:.2f}")