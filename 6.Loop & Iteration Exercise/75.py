''' Input a number from user and find first and last digit of number using loop.'''

num = int(input("Enter a number: "))

last_digit = num % 10

digit = len(str(num))
 
first_digit = num // pow(10, digit-1)
    
print("First digit is ", first_digit)
print("Last digit is ", last_digit)