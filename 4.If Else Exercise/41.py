'''check whether a number is divisible by 5 and 11 or not using if else.'''

num = int(input("Enter a number : "))

if (not(num % 5)) and (not(num % 11)):
    print("The number is divisilbe by 5 and 11.")
else:
    print("The number is not divisilbe by 5 and 11.")