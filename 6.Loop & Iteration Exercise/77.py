'''Input a number from user and swap first and last digit of the given number.'''

import math

num = int(input("Enter any number: "))
original = abs(num)

last_digit = original % 10

digit = int(math.log10(original))

first_digit = original // pow(10, digit)

swappednum = last_digit * int(round(pow(10, digit)))
swappednum += original % int(round(pow(10, digit)))
swappednum -= last_digit
swappednum += first_digit

print("Original number is ", num)
print("Number after swaping first and last digit: ", swappednum)
