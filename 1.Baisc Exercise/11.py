'''Enter two angles of a triangle and find the missing angle.'''

x = int(input("Enter A angle of a triangle: "))
y = int(input("Enter B angle of a triangle: "))

z = 180 - (x + y)

print("The third angle of a triangle is", z)