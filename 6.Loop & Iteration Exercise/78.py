'''Input a number and calculate sum of digits using for loop.'''

num = int(input("Enter any number: "))
sum = 0

while (num !=0 ):
    sum += num % 10
    num = num // 10

print("Sum of digit is ", sum)