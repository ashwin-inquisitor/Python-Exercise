'''Enter three numbers from user and
 find maximum between three numbers
 using conditional/ternary operator ?:'''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

max_num = a if (a > b & a > c) else (b if b > c else c)

print("The maximum number is " +str(max_num))