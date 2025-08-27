'''Input a number and find sum of first and last digit of the number using for loop.'''

num = int(input("Enter a number to find the sum of first and last digit: "))

last_digit = num % 10

digits = len(str(num))
first_digit = num // pow(10, digits - 1)

sum = first_digit + last_digit

print("The sum of first and last digit is ", sum)