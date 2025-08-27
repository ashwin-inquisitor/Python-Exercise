'''find the square root'''

import math

num = float(input("Enter a number to find it's square root : "))

if num >= 0:
    sqrt = math.sqrt(num)
    print("square root of a {num} is", sqrt)
else:
    print("Cannot print square root of negative number")
