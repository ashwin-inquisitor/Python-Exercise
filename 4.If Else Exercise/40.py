'''input any number from user and check whether the given number is positive, negative or zero'''

num = int(input("Enter a number : "))

if num > 0:
    print(str(num)+" is psitive.")
elif num < 0:
    print(str(num)+" is negative.")
else:
    print(str(num)+" is zero.")